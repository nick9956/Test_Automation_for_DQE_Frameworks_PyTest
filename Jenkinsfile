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
                    // Check if virtual environment exists
                    if (fileExists("${VENV}")) {
                        echo "Virtual environment found."
                    }
                    else {
                    // Create a new virtual environment
                    echo "Creating a new virtual environment."
                    sh 'python3 -m venv ${VENV}'
                    sh 'ls -la ${VENV}/bin' // List contents to verify creation
                    // Install Poetry in the virtual environment
                    sh '''#!/bin/bash
                    . ${VENV}/bin/activate
                    pip install poetry
                    '''
                    }                    
                } 
                // Install or update Poetry in the virtual environment
                sh '''#!/bin/bash
                . ${VENV}/bin/activate
                pip install poetry || pip install --upgrade poetry
                '''               
            }
        }

        stage('Set Up Credentials') {
            steps {
                script {
                    withCredentials([
                        string(credentialsId: 'db-server', variable: 'DB_SERVER'),
                        string(credentialsId: 'db-port', variable: 'DB_PORT'),
                        string(credentialsId: 'db-username', variable: 'DB_USERNAME'),
                        string(credentialsId: 'db-password', variable: 'DB_PASSWORD')
                    ]) {
                        // Write credentials to config file
                        writeFile file: "${DATABASE_CONFIG_FILE}", text: """
                        [DatabaseConfig]
                        server=${DB_SERVER}
                        port=${DB_PORT}
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
                . ${VENV}/bin/activate
                poetry install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''#!/bin/bash
                . ${VENV}/bin/activate
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