pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install numpy pytest
                '''
            }
        }
        stage('Run Automated Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest -v
                '''
            }
        }
    }
}
