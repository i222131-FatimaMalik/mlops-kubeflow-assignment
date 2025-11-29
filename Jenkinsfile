pipeline {
    agent any

    environment {
        // Name your Python virtual environment folder
        VENV = "venv"
    }

    stages {

        stage('Environment Setup') {
            steps {
                echo "Setting up environment..."
                // Checkout code from GitHub
                checkout scm

                // Install Python and virtual environment
                sh 'python -m venv ${VENV}'
                sh '''
                ${VENV}/Scripts/pip install --upgrade pip
                ${VENV}/Scripts/pip install -r requirements.txt
                '''
            }
        }

        stage('Pipeline Run') {
            steps {
                echo "Running MLflow pipeline..."
                // Run your pipeline script
                sh '${VENV}/Scripts/python pipeline.py'
            }
        }

        stage('Testing & Validation') {
            steps {
                echo "Checking outputs..."
                // Optional: check if model file and metrics exist
                sh '''
                if [ ! -f model.joblib ]; then
                    echo "Model file not found!"
                    exit 1
                fi

                if [ ! -f metrics.txt ]; then
                    echo "Metrics file not found!"
                    exit 1
                fi
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline ran successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs.'
        }
    }
}
