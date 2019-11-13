pipeline {
    agent any
    environment {
		branch = BRANCH_NAME.replaceAll('/','-')
		container_name = "xml_unittests_${branch}_${BUILD_ID}_${GIT_COMMIT}"
        VERSION = readFile(env.WORKSPACE+"/VERSION").trim()
    }
    stages {
		stage("Create results directory") {
			steps {
					sh """
					mkdir ${WORKSPACE}/results
					chmod 777 ${WORKSPACE}/results
					"""
		}
	}
        stage("Run the unit tests") {
            steps {
                script {
                    sh """
					docker run --name xml_unit_tests --rm -u appuser -v ~/trunk/ts_xml/:/home/appuser/trunk/ts_xml -w /home/appuser/trunk/ts_xml/tests --entrypoint "pytest" lsstts/robot:latest -o cache_dir=${WORKSPACE}/results -ra --junitxml=${WORKSPACE}/results/results.xml
					echo "Test complete"
					"""
                }
            }
        }
	}
}
