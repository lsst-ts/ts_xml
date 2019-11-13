pipeline {
    agent any
    environment {
		branch = BRANCH_NAME.replaceAll('/','-')
		container_name = "xml_unittests_${branch}_${BUILD_ID}_${GIT_COMMIT}"
        VERSION = readFile(env.WORKSPACE+"/VERSION").trim()
    }
    stages {
		stage("Pre-build cleanup") {
			steps {
					sh """
					echo ${WORKSPACE}
					rm -r ${WORKSPACE}/results
					"""
			}
		}
		stage("Create results directory") {
			steps {
					sh """
					mkdir -p ${WORKSPACE}/results
					chmod 777 ${WORKSPACE}/results
					"""
			}
		}
        stage("Run the unit tests") {
            steps {
                script {
                    sh """
					docker run --name ${container_name} --rm -v ${WORKSPACE}:/home/appuser/trunk/ts_xml -w /home/appuser/trunk/ts_xml --entrypoint "pytest" lsstts/robot:latest -ra --junitxml=results/results.xml
					echo "Test complete"
					"""
                }
            }
        }
	}
}
