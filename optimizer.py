import pandas as pd
from pulp import LpProblem, LpMaximize, LpVariable, lpSum
from fpl_data import load_current_season, load_historical_data, fetch_fixtures
from model import train_model, apply_model

# Constants and configuration loaded from config.py
from config import BUDGET, MAX_FROM_TEAM, FORMATION_OPTIONS

# Optimize team based on given formation and budget
def optimize_team(players, formation):
    prob = LpProblem("FPL_Team_Selection", LpMaximize)
    vars = {i: LpVariable(f"player_{i}", cat="Binary") for i in players.index}

    prob += lpSum(players.loc[i, 'expected_points'] * vars[i] for i in players.index)
    prob += lpSum(vars[i] for i in players.index) == 15
    prob += lpSum(players.loc[i, 'cost'] * vars[i] for i in players.index) <= BUDGET

    for pos in ['GK', 'DEF', 'MID', 'FWD']:
        count = 1 if pos == 'GK' else formation[pos]
        prob += lpSum(vars[i] for i in players.index if players.loc[i, 'position'] == pos) >= count

    for team in players['team_name'].unique():
        prob += lpSum(vars[i] for i in players.index if players.loc[i, 'team_name'] == team) <= MAX_FROM_TEAM

    prob.solve()

    selected = players[[vars[i].value() == 1 for i in players.index]].copy()
    return selected

# Adjust expected points based on opponent difficulty for the selected gameweek
def adjust_for_fixtures(df, fixtures, gameweek=1):
    player_fixtures = fixtures[fixtures['event'] == gameweek]
    player_fixtures['difficulty_adjustment'] = player_fixtures.apply(
        lambda row: 0.5 if row['team_a_difficulty'] > 3 else 1 if row['team_h_difficulty'] > 3 else 1.2,
        axis=1
    )
    df['expected_points'] = df['expected_points'] * df['team_name'].apply(
        lambda team: player_fixtures[player_fixtures['team_a'] == team]['difficulty_adjustment'].values[0] if len(player_fixtures[player_fixtures['team_a'] == team]) > 0 else 1
    )
    return df

# Main function to get the best optimized team
def generate_best_team():
    hist = load_historical_data()
    model = train_model(hist)
    current = load_current_season()
    fixtures = fetch_fixtures()

    # Apply machine learning model
    current = apply_model(model, current)

    # Adjust for fixture difficulty
    gameweek_choice = 1  # Modify this to dynamically select the gameweek
    current = adjust_for_fixtures(current, fixtures, gameweek_choice)

    # Choose best formation
    team, formation = find_best_team(current)
    return team
