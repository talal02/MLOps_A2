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
        bat 'docker image rm mlops_a2 || echo Image mlops_a2 Already Removed'
        bat 'docker stop mlops_a2 || true && docker rm mlops_a2 || true'
        bat 'docker build -t mlops_a2 .'
        echo 'Running docker image'
        bat 'docker run --name mlops_a2 -p 8000:5000 mlops_a2'
      }
    }
  }
}