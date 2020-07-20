pipeline {
  agent any

  stages {
    stage('Chekout') {
      steps {
        // это делать не надо
        // deleteDir()
        // т.к. следующий шаг
        // checkout scm
        // также делается автоматически
        sh '''
          git log HEAD^..HEAD --pretty="%h %an - %s"
          pwd
          chmod 755 ./sh/*.sh
          ls -l ./sh/*
        '''
      }
    }
      stage('Build') {
          steps {
            sh '''
                pyupdater build --console --app-version `./sh/getversion.sh` --add-data "../../pyupdatermywx/lua;pyupdatermywx/lua" run.py
                pyupdater pkg --process --sign
            '''
          }
        }
    }

  post {
    success {
      emailext (
        subject: "Jenkins Build ${currentBuild.currentResult}: Job: [${env.JOB_NAME}] build #${env.BUILD_NUMBER}",
        body: "<b><font color='green'>${currentBuild.currentResult}</font></b>: Job: [${env.JOB_NAME}] build <b>#${env.BUILD_NUMBER}</b><br>More info at: ${env.BUILD_URL}",
        recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']]
      )
    }
    failure {
       emailext (
        subject: "Jenkins Build FAILURE: Job: [${env.JOB_NAME}] build #${env.BUILD_NUMBER}",
        body: "<b><font color='red'>FAILURE</font></b>: Job: [${env.JOB_NAME}] build <b>#${env.BUILD_NUMBER}</b><br>More info at: ${env.BUILD_URL}",
        recipientProviders: [[$class: 'DevelopersRecipientProvider'], [$class: 'RequesterRecipientProvider']]
      )
    }
  }
}
