pipeline {
    agent any

    environment {
        IMAGE_NAME = "akibatra25/imt2023025-todo"
        DOCKERHUB = credentials('dockerhub-creds-3025')
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Python + pip') {
            steps {
                bat """
                where python
                python --version
                pip --version
                """
            }
        }

        stage('Install dependencies') {
            steps {
                bat "python -m pip install --upgrade pip"
            }
        }

        stage('Install requirements') {
            steps {
                bat "python -m pip install -r requirements.txt"
            }
        }

        stage('Run tests') {
            steps {
                bat "python -m pytest"
            }
        }

        stage('Build Docker image') {
            steps {
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Push Docker image') {
            steps {
                bat "docker login -u %DOCKERHUB_USR% -p %DOCKERHUB_PSW%"
                bat "docker push %IMAGE_NAME%"
            }
        }
    }
}
