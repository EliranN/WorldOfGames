pipeline {
      environment {
        url_ip = "172.18.0.2"
        port_id = "8777"
      }
  agent any
  stages {
    stage('1. Cloning Git') {
      steps {
        echo 'Cloning...'
        git credentialsId: 'GitHub-Creds', url: 'https://github.com/EliranN/WorldOfGames'
        bat 'docker system prune -af'
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
            bat "python tests\\e2e.py ${env.url_ip} ${env.port_id}"
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
              withCredentials([usernamePassword(credentialsId: 'Docker-hub-creds', passwordVariable: 'PASSWORD',
               usernameVariable: 'USERNAME')]) {
                bat 'docker login -u ${USERNAME} -p ${PASSWORD}'}
              bat 'docker login -u nadjmi -p *****'
              bat 'docker-compose push'
              bat 'docker-compose down --rmi all'
        }
       }
       }