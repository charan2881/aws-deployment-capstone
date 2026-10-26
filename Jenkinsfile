pipeline {
    agent any

    environment {
        AWS_REGION = 'eu-north-1'
        AWS_ACCOUNT_ID = '863555332085'
        ECR_REPOSITORY = 'aws-deployment-capstone'
        IMAGE_TAG = 'latest'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Downloading source code from GitHub...'
                checkout scm
            }
        }

        stage('Check Tools') {
            steps {
                bat '"C:\\Program Files\\Git\\cmd\\git.exe" --version'
                bat '"C:\\Users\\user\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" --version'
                bat '"C:\\Users\\user\\AppData\\Local\\Programs\\Amazon\\AWSCLIV2\\aws.exe" --version'
            }
        }

        stage('Check AWS Credentials') {
            steps {
                withCredentials([
                    [$class: 'AmazonWebServicesCredentialsBinding',
                     credentialsId: 'aws-jenkins-creds']
                ]) {
                    bat '''
                    "C:\\Users\\user\\AppData\\Local\\Programs\\Amazon\\AWSCLIV2\\aws.exe" sts get-caller-identity --region %AWS_REGION%
                    '''
                }
            }
        }

        stage('Check Docker Engine') {
            steps {
                bat '"C:\\Users\\user\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" info'
            }
        }

        stage('Login to ECR') {
            steps {
                withCredentials([
                    [$class: 'AmazonWebServicesCredentialsBinding',
                     credentialsId: 'aws-jenkins-creds']
                ]) {
                    bat '''
                    "C:\\Users\\user\\AppData\\Local\\Programs\\Amazon\\AWSCLIV2\\aws.exe" ecr get-login-password --region %AWS_REGION% | "C:\\Users\\user\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" login --username AWS --password-stdin %AWS_ACCOUNT_ID%.dkr.ecr.%AWS_REGION%.amazonaws.com
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '"C:\\Users\\user\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t %ECR_REPOSITORY%:%IMAGE_TAG% .'
            }
        }

        stage('Tag Docker Image') {
            steps {
                bat '"C:\\Users\\user\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" tag %ECR_REPOSITORY%:%IMAGE_TAG% %AWS_ACCOUNT_ID%.dkr.ecr.%AWS_REGION%.amazonaws.com/%ECR_REPOSITORY%:%IMAGE_TAG%'
            }
        }

        stage('Push Image to ECR') {
            steps {
                bat '"C:\\Users\\user\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" push %AWS_ACCOUNT_ID%.dkr.ecr.%AWS_REGION%.amazonaws.com/%ECR_REPOSITORY%:%IMAGE_TAG%'
            }
        }
    }

    post {
        success {
            echo 'Docker image successfully pushed to Amazon ECR!'
        }
        failure {
            echo 'Pipeline failed. Check the failed stage in the Jenkins console output.'
        }
    }
}
