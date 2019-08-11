pipeline {
	agent any
	stages {
		stage('Testing') {
			steps {
				sh "echo Super & exit 0"
			}
		}
		stage('SonarQube') {
	    environment {
        scannerHome = tool 'Code IRM'
			}
			steps {
				withSonarQubeEnv('Code IRM') {
					sh "${scannerHome}/bin/sonar-scanner"
        }
			}
		}
	}
	post {
		always {
			notifySlack(currentBuild.currentResult, 'UM861B4HE')
		}
	}
}

