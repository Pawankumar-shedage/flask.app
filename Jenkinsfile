pipeline {
    agent any
      
/*    environment {
        DOCKER_TOKEN = credentials('DOCKER_ACCESS_TOKEN')
    }
*/
    stages {
        stage('Pull data form git') {
            steps {
                git branch: 'main', url: 'https://github.com/Pawankumar-shedage/flask.app.git'
            }
        }
        
        stage('Delete existing Image') {
              steps {
                  sh 'ls -l'
                  sh '''
                      if docker image inspect gaming7761/myweb > /dev/null 2>&1; then
                          echo "Image exists. Deleting..."
                          docker image rm --force gaming7761/myweb
                      else
                          echo "Image does not exist. Skipping deletion."
                      fi
                  '''
              }
        }

        stage('Build Image') {
            steps {
                sh 'ls -l'
                sh 'docker build -t gaming7761/myweb .'
            }
        }
       
        stage ('docker login'){
            steps {
                sh 'echo dckr_pat_kF7Lo8M9JBru8jqM01UTWVbE8os | docker login -u gaming7761 --password-stdin'
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
        
	      stage('create service') {
            steps {
                sh 'docker service create --name myservice -p 4000:4000 --replicas 2 gaming7761/myweb'
            }
        }
        
        stage ('docker logout') {
            steps {
                sh 'echo "Loggin out from docker hub" '
                sh 'docker logout' 
            }
        }

    }
}

