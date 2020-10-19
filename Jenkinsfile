pipeline {
      environment {
        url_ip = "127.0.0.1"
        port_id = "8777"
      }
  agent {
        node {
            label 'windows'
        }
    }
  stages {
    stage('1. Cloning Git') {
      steps {
        echo 'Cloning...'
        git 'https://github.com/EliranN/WorldOfGames'
      }
    }
    stage('2. Building Image') {
      steps{
      echo 'Building...'
      bat 'docker-compose pull'
      bat 'docker-compose build'
      }
    }
    stage('3. Running Container') {
      steps{
      echo 'Running...'
      bat 'docker-compose up -d'
      }
    }
    stage('4. Testing Application') {
      steps {
      echo 'Testing...'
            script {
        try {
            bat "python3 tests\\e2e.py ${env.url_ip} ${env.port_id}"
        } catch (err) {
                        currentBuild.result='FAILURE'
                    }
        }
      }
    }
  }
  post {
        always {
              echo '5. Finalizing...'
              bat 'docker login -u nadjmi -p *****'
              bat 'docker-compose push'
              bat 'docker-compose down --rmi all'
        }
       }
       }