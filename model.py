import pandas as pd
from sklearn.model_selection import train_test_split
from lightgbm import LGBMRegressor

# Train a model to predict player points based on historical data
def train_model(hist_df):
    print("Columns in historical data:", hist_df.columns)  # Add this line
    hist_df = hist_df.dropna(subset=['minutes'])
    pos_encoded = pd.get_dummies(hist_df['position_name'])  # This line might fail
    features = pd.concat([pos_encoded, hist_df[['minutes', 'goals_scored', 'assists', 'clean_sheets']]], axis=1)
    target = hist_df['points']
    model = LGBMRegressor()
    model.fit(features.fillna(0), target)
    return model


# Apply the model to current season data to predict expected points
def apply_model(model, current_df):
    pos_encoded = pd.get_dummies(current_df['position'])
    for pos in ['GK', 'DEF', 'MID', 'FWD']:
        if pos not in pos_encoded.columns:
            pos_encoded[pos] = 0
    X = pd.concat([pos_encoded, current_df[['minutes', 'goals_scored', 'assists', 'clean_sheets']]], axis=1).fillna(0)
    current_df['expected_points'] = model.predict(X)
    return current_df
