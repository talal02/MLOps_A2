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
        bat 'more app.py'
        echo 'Running docker image'
        bat 'docker run --name mlops_a2 -p 8000:5000 mlops_a2'
      }
    }
  }
}