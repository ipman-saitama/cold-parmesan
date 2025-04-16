import pandas as pd
import requests

# Fetch current season data from FPL API
def load_current_season():
    r = requests.get("https://fantasy.premierleague.com/api/bootstrap-static/")
    data = r.json()
    elements = pd.DataFrame(data['elements'])
    teams = pd.DataFrame(data['teams'])
    elements['position'] = elements['element_type'].map(POSITION_MAP)
    elements['team_name'] = elements['team'].apply(lambda x: teams.iloc[x-1]['name'])
    elements['cost'] = elements['now_cost'].astype(int)
    return elements

# Load historical season data
def load_historical_data():
    url_2022_23 = 'https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2022-23/cleaned_players.csv'
    url_2023_24 = 'https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2023-24/cleaned_players.csv'
    data_2022_23 = pd.read_csv(url_2022_23)
    data_2022_23['season'] = '2022/23'
    data_2023_24 = pd.read_csv(url_2023_24)
    data_2023_24['season'] = '2023/24'
    df = pd.concat([data_2022_23, data_2023_24], ignore_index=True)
    df = df.rename(columns={'position': 'position_name', 'total_points': 'points'})
    return df

# Fetch fixtures and difficulty data
def fetch_fixtures():
    r = requests.get("https://fantasy.premierleague.com/api/fixtures/")
    fixtures = pd.DataFrame(r.json())
    fixtures = fixtures[['event', 'team_a', 'team_h', 'team_a_difficulty', 'team_h_difficulty']]
    return fixtures
