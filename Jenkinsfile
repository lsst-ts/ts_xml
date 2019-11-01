pipeline {
    agent any
    environment {
	    branch = BRANCH_NAME.replaceAll('/','-')
        container_name = "robot_${branch}_${BUILD_ID}_${GIT_COMMIT}"
        VERSION = readFile(env.WORKSPACE+"/VERSION").trim()
    }

    stages {
		stage("Cleanup before build") {
			steps {
				sh """
				"""
				}
			}
        stage("Run the unit tests") {
            steps {
                script {
                    sh """
					python env.WORKSPACE+"/tests/*py"
					echo "Test complete"
					"""
                }
            }
        }
	}
    post {
        always {
            // Copy tests results
			script {
				sh """
				"""
			}
		}
        cleanup {
            sh """
            """
        }
    }
}
