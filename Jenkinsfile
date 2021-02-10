pipeline{
    // agent {
    //     docker { 
    //         image 'node:lts' 
    //         args '-p 5000:5000'
    //         } 
    // }
    agent any
    options {
        timeout(time: 5, unit: 'MINUTES') 
        skipDefaultCheckout true
    }  
    tools {nodejs "python"}
    stages{
        stage('Cloning Repository'){
          steps{     
            script {
                  Exception caughtException = null
                  catchError(buildResult: 'SUCCESS', stageResult: 'ABORTED') { 
                    try { 
                        echo "Cloning Repo"
                        git credentialsId: 'github-credential', url: 'https://github.com/pai12345/Andromeda_SendEmail.git'  
                    } catch (Throwable e) {
                        caughtException = e
                    }
                  }
                  if (caughtException) {
                        error caughtException.message
                    }
            }
          }
        }
        stage('Build'){
          steps{
            script {
                  Exception caughtException = null
                  catchError(buildResult: 'SUCCESS', stageResult: 'ABORTED') { 
                  try { 
                    sh '''
                       pip install -r requirements.txt
                       python index.py
                      '''
                  } catch (Throwable e) {
                      caughtException = e
                    }                  
                  }
                   if (caughtException) {
                        error caughtException.message
                    }
            }
          }
        }
    }
    post {
        always {
          echo "Cleaning Workspace"
          cleanWs()
        }
    }
}