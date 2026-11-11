pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt pytest'
            }
        }
        stage('Run Automated Tests') {
            steps {
                bat 'pytest -v'
            }
        }
    }
}
