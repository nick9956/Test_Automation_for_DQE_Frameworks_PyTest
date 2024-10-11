pipeline {
    agent {
        docker {
            image 'python:3.11.2'
        }
    }
    environment {
        DB_CONFIG_FILE = 'db/db.cfg'
    }
    stages {
        stage('Setup') {
            steps {
                sh 'pip install poetry'
                sh 'poetry config virtualenvs.create false'
                sh 'poetry install'
            }
        }
        stage('Prepare DB Config') {
            steps {
                withCredentials([file(credentialsId: 'db-config', variable: 'DB_CONFIG')]) {
                    sh 'cp $DB_CONFIG $DB_CONFIG_FILE'
                }
            }
        }
        stage('Test') {
            steps {
                sh 'pytest'
            }
        }
    }
    post {
        always {
            sh 'rm -f $DB_CONFIG_FILE'
        }
    }
}