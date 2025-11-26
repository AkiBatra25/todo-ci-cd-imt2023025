pipeline {
    agent any
    tools {
        python 'python3'   // This must match the name you added in Global Tool Configuration
    }

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

        stage('Install dependencies') {
            steps {
                bat 'python -m pip install --upgrade pip'
            }
        }

        stage('Install requirements') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Run tests') {
            steps {
                bat 'pytest'
            }
        }

        stage('Build Docker image') {
            when { expression { currentBuild.currentResult == "SUCCESS" } }
            steps {
                bat "docker build -t %IMAGE_NAME% ."
            }
        }

        stage('Push Docker image') {
            when { expression { currentBuild.currentResult == "SUCCESS" } }
            steps {
                bat "docker login -u %DOCKERHUB_USR% -p %DOCKERHUB_PSW%"
                bat "docker push %IMAGE_NAME%"
            }
        }
    }

}
