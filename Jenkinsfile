```groovy
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
                bat 'git --version'
                bat 'docker --version'
                bat 'aws --version'
            }
        }
    }
}
```
