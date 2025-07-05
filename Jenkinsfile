pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/fidanalizada19/telco_churn_prediction.git'
            }
        }
        stage('Install Requirements') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Train Model') {
            steps {
                sh 'python models/telco_model.py'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'pytest tests/'
            }
        }
        stage('Docker Build & Run') {
            steps {
                sh 'docker-compose -f docker-compose.prod.yml up -d --build'
            }
        }
    }
}
