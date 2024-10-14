pipeline {
    agent any
    stages {
        stage('Prepare Environment') {
            steps {
                script {
                    // Retrieve DB config from Jenkins credentials and write to db.cfg
                    withCredentials([file(credentialsId: 'db-config', variable: 'DB_CONFIG')]) {
                        sh 'cp $DB_CONFIG db/db.cfg'
                    }
                    // Install project dependencies using Poetry
                    sh 'poetry install'
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Running tests using Pytest
                    sh 'poetry run pytest'
                }
            }
        }
    }
}