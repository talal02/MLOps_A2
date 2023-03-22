pipeline {
  agent any
  stages {
    stage('Checkout') {
      steps{
        checkout scm
      }
    }
    stage('Run') {
      steps {
        script {
          try {
            bat 'docker stop mlops_a2'
          } catch(err) {
            bat 'echo Container mlops_a2 Already Stopped'
          }
          try {
              bat 'docker rm mlops_a2'
          } catch(err1) {
            bat 'echo done'
          }
          try {
            bat 'docker image rm mlops_a2'
          } catch (err) {
            bat 'echo Image mlops_a2 Already Removed'
          }
          bat 'echo bingo!'
          bat 'docker build -t mlops_a2 .'
          bat 'docker login -u talal02 -p T123456??'
          bat 'docker tag mlops_a2 talal02/mlops_a2'
          bat 'docker push talal02/mlops_a2'
          echo 'Running docker image'
          bat 'docker run --name mlops_a2 -p 8000:5000 mlops_a2'
        }
      }
    }
  }
}