pipeline {
    agent any

    stages {
        stage('Pull data form git') {
            steps {
                git branch: 'main', url: 'https://github.com/Pawankumar-shedage/flask.app.git'
            }
        }
        
        stage('Delete existing Image') {
            steps {
                sh 'ls -l'
                sh 'docker image rm gaming7761/myweb'
            }
        }

        stage('Build Image') {
            steps {
                sh 'ls -l'
                sh 'docker build -t gaming7761/myweb .'
            }
        }
        
        stage('push image') {
            steps {
                sh 'docker push gaming7761/myweb'
            }
        }

        stage('remove existing service') {
            steps {
                sh 'docker service rm mywebservice'
            }
        }
        
	      stage('creat service') {
            steps {
                sh 'docker service create --name myservice -p 4000:4000 --replicas 2 gaming7761/myweb'
            }
        }
    }
}
