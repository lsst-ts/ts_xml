pipeline {
    agent any
    environment {
        branch = BRANCH_NAME.replaceAll('/','-')
        job_name = JOB_NAME.replaceAll(' ','_').replaceAll('/','-').replaceAll('%2F','-')
        container_name = "xml_unittests_${job_name}_${branch}_${BUILD_ID}_${GIT_COMMIT}"
        VERSION = readFile(env.WORKSPACE+"/VERSION").trim()
    }
    stages {
        stage("Pre-build cleanup") {
             steps {
                  sh """
                  git clean -dxf
                  """
             }
        }
        stage("Create results directory") {
            steps {
                sh """
                mkdir -p ${WORKSPACE}/tests/results
                chmod 777 ${WORKSPACE}/tests/results
                """
            }
        }
        stage("Pull down the docker image") {
            steps {
                script {
                    sh """
                    docker pull lsstts/robot:latest
                    """
            }
        }
    }
        stage("Run the unit tests") {
            steps {
                script {
                    sh """
		    docker run --name ${container_name} -di --rm -v ${WORKSPACE}:/home/appuser/trunk/ts_xml -w /home/appuser/trunk/ts_xml lsstts/robot:latest 
                    docker exec -u appuser -w /home/appuser/trunk/ts_xml ${container_name} sh -c "python3 -m pip install -r test_requirements.txt -e . && \
                        pytest -ra -o junit_family=xunit2 --junitxml=tests/results/results.xml"
                    docker stop ${container_name}
		    echo "Test complete"
		    """
                }
            }
        }
    }
    post {
        always {
            junit 'tests/results/results.xml'
        }
    }
}
