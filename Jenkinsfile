pipeline {
    agent any

    environment {
        VENV = 'venv'
    }

    triggers {
        pollSCM('H/2 * * * *')  // checks GitHub every 2 minutes
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                bat '''
                python -m venv %VENV%
                call %VENV%\\Scripts\\activate
                python -m pip install --upgrade pip
                pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '''
                call %VENV%\\Scripts\\activate
                pytest tests -v --html=reports\\report.html --self-contained-html
                '''
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/**/*', allowEmptyArchive: true

            publishHTML([
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'UI Automation Test Report',
                alwaysLinkToLastBuild: true,
                keepAll: true,
                allowMissing: true
            ])
        }
    }
}
