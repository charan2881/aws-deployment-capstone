pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code is ready for the deployment pipeline.'
            }
        }

        stage('Check Tools') {
            steps {
                sh 'git --version'
                sh 'docker --version'
                sh 'aws --version'
            }
        }
    }
}
