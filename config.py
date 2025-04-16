# Configuration for FPL Optimizer

BUDGET = 1000
MAX_FROM_TEAM = 3
MAX_PLAYERS = 15
POSITION_MAP = {1: 'GK', 2: 'DEF', 3: 'MID', 4: 'FWD'}

FORMATION_OPTIONS = [
    {'GK': 1, 'DEF': 3, 'MID': 5, 'FWD': 2},
    {'GK': 1, 'DEF': 4, 'MID': 4, 'FWD': 2},
    {'GK': 1, 'DEF': 3, 'MID': 4, 'FWD': 3},
    {'GK': 1, 'DEF': 4, 'MID': 3, 'FWD': 3},
    {'GK': 1, 'DEF': 5, 'MID': 3, 'FWD': 2},
]

# Logic for calculating team and point adjustments
INJURY_THRESHOLD = 50  # Injury threshold percentage
