pipeline {
    agent any

   

    environment {
        PYTHON_ENV = 'venv'
    }

    triggers {
        // Poll GitHub every 5 minutes
        pollSCM('H/5 * * * *')
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Python Environment') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            python -m venv ${PYTHON_ENV} || true
                            source ${PYTHON_ENV}/bin/activate
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    } else {
                        bat '''
                            python -m venv %PYTHON_ENV%
                            call %PYTHON_ENV%\\Scripts\\activate
                            pip install --upgrade pip
                            pip install -r requirements.txt
                        '''
                    }
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    if (isUnix()) {
                        sh '''
                            source ${PYTHON_ENV}/bin/activate
                            pytest tests -v --html=reports/report.html --self-contained-html
                        '''
                    } else {
                        bat '''
                            call %PYTHON_ENV%\\Scripts\\activate
                            pytest tests -v --html=reports/report.html --self-contained-html
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts artifacts: 'reports/**/*', allowEmptyArchive: true

            publishHTML([
                reportDir: 'reports',
                reportFiles: 'report.html',
                reportName: 'Test Report',
                allowMissing: true,
                alwaysLinkToLastBuild: true,
                keepAll: true
            ])
        }

        failure {
            echo '❌ Tests failed — review HTML report'
        }
    }
}

