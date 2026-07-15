pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-mysql-devops:latest ./app'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker rm -f flask-test || true
                docker run -d --name flask-test -p 5000:5000 flask-mysql-devops:latest
                sleep 10
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh 'curl http://localhost:5000 || exit 1'
            }
        }

        stage('Cleanup') {
            steps {
                sh 'docker rm -f flask-test || true'
            }
        }
    }
}