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
                    // Check if the virtual environment exists, if not, create it
                    if (!fileExists("${VENV}")) {
                        echo "No virtual environment found. Creating a new one."
                        sh """
                            python3 -m venv ${VENV}
                            ls -la ${VENV}/bin
                        """
                    } else {
                        echo "Virtual environment already exists."
                    }
                }
                // Install or update Poetry in the virtual environment
                sh '''
                    source ${VENV}/bin/activate
                    pip install --upgrade pip
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
                        // Write credentials to the config file
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
                sh '''
                    source ${VENV}/bin/activate
                    poetry install
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    source ${VENV}/bin/activate
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