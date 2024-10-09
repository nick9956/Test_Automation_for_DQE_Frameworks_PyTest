pipeline {
    agent any

    environment {
        VENV = 'venv'
        DATABASE_CONFIG_FILE = 'db/db.cfg'
    }

    stages {
        stage('Prepare Environment') {
            steps {
                script {
                    if (!fileExists("${VENV}")) {
                        sh 'python3 -m venv ${VENV}'
                        echo "Virtual environment created."
                    } else {
                        echo "Virtual environment already exists."
                    }
                }
                sh '''#!/bin/bash
                cd /venv
                ls
                pwd
                source /Scripts/activate
                pip install poetry
                '''
            }
        }

        stage('Set Up Credentials') {
            steps {
                script {
                    withCredentials([
                        string(credentialsId: 'db-server', variable: 'DB_SERVER'),
                        string(credentialsId: 'db-username', variable: 'DB_USERNAME'),
                        string(credentialsId: 'db-password', variable: 'DB_PASSWORD')
                    ]) {
                        writeFile file: "${DATABASE_CONFIG_FILE}", text: """
                        [DatabaseConfig]
                        server=${DB_SERVER}
                        database=TRN
                        username=${DB_USERNAME}
                        password=${DB_PASSWORD}
                        """
                    }
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''#!/bin/bash
                source $WORKSPACE/${VENV}/bin/activate
                poetry install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''#!/bin/bash
                source $WORKSPACE/${VENV}/bin/activate
                poetry run pytest
                '''
            }
            post {
                always {
                    archiveArtifacts artifacts: 'report.html', fingerprint: true
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution complete!'
        }
    }
}