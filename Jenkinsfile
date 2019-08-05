pipeline {
    agent any
    environment {
        container_name = "robot_${BUILD_ID}_${GIT_COMMIT}"
        VERSION = readFile(env.WORKSPACE+"/VERSION").trim()
    }

    stages {
		stage("Cleanup before build") {
			steps {
				sh """
				rm -rf ${WORKSPACE}/robot
				rm -rf ${WORKSPACE}/rbtxml
				"""
				}
			}
        stage("Clone robotframework_ts_xml") {
            steps {
                sh """
				mkdir ${WORKSPACE}/robot
				chmod 777 ${WORKSPACE}/robot
                git clone https://github.com/lsst-ts/robotframework_ts_xml.git ${WORKSPACE}/rbtxml || echo Robotframework already here.
                """
            }
        }
        stage("Run the Robot-Framework tests") {
            steps {
                script {
                    sh """
					docker run --name ${container_name} \
					-v ${WORKSPACE}/:/home/appuser/trunk/ts_xml \
					-v ${WORKSPACE}/rbtxml:/home/appuser/trunk/robotframework_ts_xml \
					-v ${WORKSPACE}/robot:/home/appuser/Reports \
					-w /home/appuser/trunk/robotframework_ts_xml \
					--entrypoint "robot" lsstts/robot:latest \
					--outputdir /home/appuser/Reports --variable ContInt:true -e skipped \
					--noncritical TSS* --noncritical TPC* --noncritical TSEIA* --noncritical DM* \
					--variable version:${env.VERSION} -A XML_Validation.list
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
				docker cp ${container_name}:/home/appuser/Reports ${WORKSPACE}/robot
				"""
			}
			// Publish the HTML report
            publishHTML (target: [
                allowMissing: false,
                alwaysLinkToLastBuild: false,
                keepAll: true,
                reportDir: "${WORKSPACE}/robot",
                reportFiles: 'report.html',
                reportName: "Report"
              ])
			// Publish RobotFramework report
			step ([
				$class: 'RobotPublisher', 
				disableArchiveOutput: false, 
				enableCache: true, 
				logFileName: 'log.html', 
				onlyCritical: true, 
				otherFiles: '', 
				outputFileName: 'output.xml', 
				outputPath: 'robot', 
				passThreshold: 100.0, 
				reportFileName: 'report.html', 
				unstableThreshold: 95.0
			])
		}
        cleanup {
            sh """
            docker rm ${container_name}
            """
        }
    }
}
