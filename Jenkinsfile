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
                }
            }
        }
        stage('Test') {
            steps {
                script {
                    // Running tests using Podman
                    sh 'pytest'
                }
            }
        }
    }
}