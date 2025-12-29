pipeline {
  agent any

  environment {
    VENV = "venv"
  }

  triggers {
    pollSCM('H/5 * * * *')
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Setup Python') {
      steps {
        bat """
        python -m venv %VENV%
        call %VENV%\\Scripts\\activate
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        """
      }
    }

    stage('Load Environment Variables') {
      steps {
        withCredentials([file(credentialsId: 'chosen300-env', variable: 'ENVFILE')]) {
          bat 'copy /Y "%ENVFILE%" .env'
        }
      }
    }

    stage('Run Tests') {
      steps {
        bat """
        if not exist reports mkdir reports
        call %VENV%\\Scripts\\activate
        pytest tests -v --html=reports\\report.html --self-contained-html
        """
      }
    }
  }

  post {
    always {
      archiveArtifacts artifacts: 'reports/**/*', allowEmptyArchive: true
      publishHTML([
        reportDir: 'reports',
        reportFiles: 'report.html',
        reportName: 'Selenium Test Report',
        keepAll: true
      ])
    }
  }
}
