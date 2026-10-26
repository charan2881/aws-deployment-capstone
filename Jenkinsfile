pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code downloaded successfully from GitHub.'
            }
        }

        stage('Check Tools') {
            steps {
                bat '"C:\\Program Files\\Git\\cmd\\git.exe" --version'
                bat 'docker --version'
                bat 'aws --version'
            }
        }
    }
}
