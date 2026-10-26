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
                bat '"C:\\Users\\user\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" --version'
                bat '"C:\\Users\\user\\AppData\\Local\\Programs\\Amazon\\AWSCLIV2\\aws.exe" --version'
            }
        }
    }
}
