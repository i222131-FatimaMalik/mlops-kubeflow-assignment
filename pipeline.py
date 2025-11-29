import mlflow
from src.pipeline_components import load_data, preprocess_data, train_model, evaluate_model

# Path to your dataset
DATA_PATH = "data/raw/raw_data.csv"

# MLflow experiment name
EXPERIMENT_NAME = "Boston_Housing_Experiment"

# Model and metrics output paths
MODEL_PATH = "model.joblib"
METRICS_PATH = "metrics.txt"

def main():
    # Set MLflow experiment
    mlflow.set_experiment(EXPERIMENT_NAME)
    
    with mlflow.start_run():
        # Step 1: Load data
        df = load_data(DATA_PATH)
        print(f"Data loaded. Shape: {df.shape}")

        # Step 2: Preprocess data
        X_train, X_test, y_train, y_test = preprocess_data(df)
        print(f"Train/Test split -> Train: {X_train.shape}, Test: {X_test.shape}")

        # Step 3: Train model
        model_file = train_model(X_train, y_train, MODEL_PATH)
        mlflow.log_artifact(model_file)
        print(f"Model trained and saved to {model_file}")

        # Step 4: Evaluate model
        metrics_file = evaluate_model(X_test, y_test, MODEL_PATH, METRICS_PATH)
        mlflow.log_artifact(metrics_file)
        print(f"Metrics saved to {metrics_file}")

        # Optional: Log parameters
        mlflow.log_param("model_type", "RandomForestRegressor")
        mlflow.log_param("n_estimators", 100)

if __name__ == "__main__":
    main()
