import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib

# Column names for Boston Housing dataset
COLUMN_NAMES = [
    "CRIM","ZN","INDUS","CHAS","NOX","RM","AGE","DIS",
    "RAD","TAX","PTRATIO","B","LSTAT","MEDV"
]

def load_data(csv_path: str):
    """
    Load CSV data without headers and assign column names
    """
    df = pd.read_csv(csv_path, header=None, delim_whitespace=True, names=COLUMN_NAMES)
    return df

def preprocess_data(df):
    """
    Preprocess dataset: split into features/target and train/test
    """
    X = df.drop("MEDV", axis=1)
    y = df["MEDV"]
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

def train_model(X_train, y_train, model_path="model.joblib"):
    """
    Train RandomForestRegressor and save model
    """
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    joblib.dump(model, model_path)
    return model_path

def evaluate_model(X_test, y_test, model_path="model.joblib", metrics_path="metrics.txt"):
    """
    Evaluate trained model and save metrics
    """
    model = joblib.load(model_path)
    preds = model.predict(X_test)
    
    mse = mean_squared_error(y_test, preds)
    r2 = r2_score(y_test, preds)
    
    with open(metrics_path, "w") as f:
        f.write(f"MSE: {mse}\n")
        f.write(f"R2: {r2}\n")
    
    return metrics_path
