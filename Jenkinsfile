pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt pytest'
            }
        }
        stage('Run Automated Tests') {
            steps {
                bat 'pytest -v'
            }
        }
    }
}
