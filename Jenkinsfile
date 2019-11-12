pipeline {
    agent any
    environment {
		branch = BRANCH_NAME.replaceAll('/','-')
        VERSION = readFile(env.WORKSPACE+"/VERSION").trim()
    }
    stages {
        stage("Run the unit tests") {
            steps {
                script {
                    sh """
					pip install -U --user pytest
					mkdir test_results/
					pytest tests/test*.py --junitxml=test_results/report.xml
					echo "Test complete"
					"""
                }
            }
        }
	}
    post {
        always {
			junit test_results/report.xml
		}
	}
}
