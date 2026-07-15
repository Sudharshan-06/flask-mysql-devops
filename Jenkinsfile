pipeline {
    agent any

    environment {
        IMAGE_NAME = "sudharshannnn/flask-mysql-devops"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME:latest ./app'
            }
        }

        stage('Run Container') {
            steps {
                sh '''
                docker rm -f flask-test || true
                docker run -d --name flask-test -p 5000:5000 $IMAGE_NAME:latest
                sleep 10
                '''
            }
        }

        stage('Health Check') {
            steps {
                sh 'curl http://localhost:5000'
            }
        }

        stage('Cleanup') {
            steps {
                sh 'docker rm -f flask-test || true'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                    sh 'echo $PASSWORD | docker login -u $USERNAME --password-stdin'
                }
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $IMAGE_NAME:latest'
            }
        }
    }

    post {
        always {
            sh 'docker logout || true'
        }
    }
}