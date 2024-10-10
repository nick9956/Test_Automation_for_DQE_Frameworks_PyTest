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
                    // Check if virtual environment exists, if so delete it for a clean setup
                    if (fileExists("${VENV}")) {
                        echo "Virtual environment found. Deleting..."
                        sh "rm -rf ${VENV}"
                        echo "Virtual environment deleted."
                    }
                    // Create a new virtual environment
                    echo "Creating a new virtual environment."
                    sh 'python3 -m venv ${VENV}'
                    sh 'ls -la ${VENV}/bin' // List contents to verify creation
                }
                // Install Poetry in the virtual environment
                sh '''#!/bin/bash
                . ${VENV}/bin/activate
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
                        // Write credentials to config file
                        writeFile file: "${DATABASE_CONFIG_FILE}", text: """
                        [DatabaseConfig]
                        server=${DB_SERVER}
                        database=TRN
                        username=${DB_USERNAME}
                        password=${DB_PASSWORD}
                        """
                        echo "Logging DB config file contents for debugging:"
                        sh "cat ${DATABASE_CONFIG_FILE}"
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