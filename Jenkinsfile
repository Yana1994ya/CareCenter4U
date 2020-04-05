pipeline {
    agent none
    stages {
        stage('Test') {
            agent {
                docker {
                    image 'python:3'//select python 3
                }
            }
            steps {
                withEnv(["HOME=${env.WORKSPACE}"]) {
     				sh 'pip install django --user'//install django
              		sh 'manage.py migrate'//creates the sqlite database
               		sh 'manage.py test'//run test
  				}
            }
        }
        
    }
}