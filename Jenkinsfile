pipeline {
    agent any
    environment {
        container_name = "robot_${BUILD_ID}_${GIT_COMMIT}"
        VERSION = readFile(env.WORKSPACE+"/VERSION").trim()
    }

    stages {
        stage("Clone robotframework_ts_xml") {
            steps {
                sh "git clone https://github.com/lsst-ts/robotframework_ts_xml.git rbtxml || echo Robotframework already here."
            }
        }
        stage("Run the Robot-Framework tests") {
            steps {
                script {
                    sh """
docker run --name ${container_name} \
-v ${WORKSPACE}/:/home/appuser/trunk/ts_xml \
-v ${WORKSPACE}/rbtxml:/home/appuser/trunk/robotframework_ts_xml \
-w /home/appuser/trunk/robotframework_ts_xml \
--entrypoint "robot" lsstts/robot:latest \
--outputdir /home/appuser/Reports --variable ContInt:true -e skipped \
--noncritical TSS* --noncritical TPC* --noncritical TSEIA* --noncritical DM* \
--variable version:${env.VERSION} -A XML_Validation.list
                    """
                }
            }

        }
        stage("Copy tests results") {
            steps {
                script {
                    sh """
                    docker cp ${container_name}:/home/appuser/Reports ${WORKSPACE}/robot
                    """
                }
            }
        }
    }
    post {
        always {
            // Publish the HTML report
            publishHTML (target: [
                allowMissing: false,
                alwaysLinkToLastBuild: false,
                keepAll: true,
                reportDir: "${WORKSPACE}/robot",
                reportFiles: 'index.html',
                reportName: "Report"
              ])
        }
        cleanup {
            sh """
            docker rm ${container_name}
            """
        }
    }
}
