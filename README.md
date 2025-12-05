MLflow MLOps Pipeline – Assignment
📌 Project Overview

This project demonstrates a simple end-to-end MLOps workflow using:

MLflow Pipelines – for reproducible pipeline steps

DVC (Data Version Control) – for dataset tracking and remote storage

GitHub Actions / Jenkins – for CI/CD automation

Python (scikit-learn) – for model training and evaluation

The ML problem used in this assignment is the Boston Housing Regression Task, where the goal is to predict house prices based on 13 numerical input features.

The project includes:

Data extraction from DVC remote

Preprocessing (train/test split)

Model training (Linear Regression)

Evaluation and metrics logging

CI/CD pipeline for automatic validation

⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone <your-repo-url>
cd mlops-kubeflow-assignment

2️⃣ Create a Virtual Environment
Windows:
python -m venv venv
venv\Scripts\activate

Mac/Linux:
python3 -m venv venv
source venv/bin/activate

3️⃣ Install Dependencies
pip install --upgrade pip
pip install -r requirements.txt

4️⃣ DVC Setup

This project uses DVC to track the dataset stored remotely.

Initialize DVC

(Only run this if .dvc folder is missing)

dvc init

Add Remote Storage

Example (Google Drive / S3 / Local FS — depends on your instructor):

dvc remote add -d myremote <REMOTE-URL>


To pull dataset tracked by DVC:

dvc pull


This downloads:

data/raw/data.csv

5️⃣ MLflow Setup

MLflow tracking runs locally using the default file store.

To start MLflow UI:

mlflow ui


Then visit:

http://127.0.0.1:5000

🚀 Pipeline Walkthrough

The MLflow pipeline is implemented in two files:

src/pipeline_components.py → load, preprocess, train, evaluate

pipeline.py → orchestrates the full MLflow workflow

1️⃣ Run the MLflow Pipeline

In the project root:

python pipeline.py


This performs:

✔ Load dataset using DVC
✔ Clean and preprocess
✔ Split into train/test
✔ Train Linear Regression
✔ Save trained model (model.joblib)
✔ Save evaluation metrics (metrics.txt)
✔ Log all outputs to MLflow

Sample output:

Data loaded. Shape: (506, 14)
Train/Test split -> Train: (404, 13), Test: (102, 13)
Model trained and saved to model.joblib
Metrics saved to metrics.txt

2️⃣ View MLflow Logs

Run:

mlflow ui


You will be able to see:

Model parameters

Metrics

Artifacts (model + plots + metrics)

3️⃣ Continuous Integration (CI/CD)

You can run the pipeline automatically using:

GitHub Actions → .github/workflows/mlflow-pipeline.yml

Jenkins → Jenkinsfile

Each CI pipeline includes:

Environment Setup

Pipeline Execution

Tests & Validation

A successful run ensures your ML pipeline works end-to-end on every commit.

📁 Repository Structure
.
├── data/               # DVC-tracked dataset
├── src/
│   ├── pipeline_components.py
├── pipeline.py
├── requirements.txt
├── .dvc/
├── .gitignore
├── Jenkinsfile
├── Dockerfile
└── README.md
