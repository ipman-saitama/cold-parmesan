# optimizer.py

# This function will generate the best team based on certain rules
def generate_best_team():
    # Example data (you can replace this with actual logic or data from FPL API)
    best_team = [
        {"name": "Player1", "position": "GK", "team": "TeamA", "points": 50},
        {"name": "Player2", "position": "DEF", "team": "TeamB", "points": 45},
        {"name": "Player3", "position": "DEF", "team": "TeamC", "points": 40},
        {"name": "Player4", "position": "MID", "team": "TeamD", "points": 60},
        {"name": "Player5", "position": "MID", "team": "TeamE", "points": 55},
        {"name": "Player6", "position": "FWD", "team": "TeamF", "points": 65},
    ]
    
    # For now, it simply returns a list of player names
    best_team_names = [player["name"] for player in best_team]
    
    return best_team_names
