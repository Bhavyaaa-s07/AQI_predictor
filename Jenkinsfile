pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "aqi-predictor-app"
        CONTAINER_NAME = "aqi-container"
    }

    stages {
        stage('Checkout') {
            steps {
                // Pulls the latest code from your GitHub
                git branch: 'main', url: 'https://github.com/Bhavyaaa-s07/AQI_predictor.git'
            }
        }

        stage('Train Model') {
            steps {
                // Jenkins runs your training script to generate aqi_model.pkl
                // Make sure python is in your Jenkins path
                bat 'python src/train.py' 
            }
        }

        stage('Build Docker Image') {
            steps {
                // Build the image using the Dockerfile
                bat "docker build -t ${DOCKER_IMAGE} ."
            }
        }

        stage('Deploy Locally') {
            steps {
                // Stop/Remove old container if it exists, then run on 5050
                bat "docker stop ${CONTAINER_NAME} || exit 0"
                bat "docker rm ${CONTAINER_NAME} || exit 0"
                bat "docker run -d -p 5050:8501 --name ${CONTAINER_NAME} ${DOCKER_IMAGE}"
            }
        }
    }
}