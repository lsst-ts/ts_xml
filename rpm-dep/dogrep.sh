#!/bin/sh
find $1 -type f -not -path "./ts_xml/*" -not -path "./grepper/*" -name '*.py'        -exec grep -l SALPY_$2 {} \; > refs/$2
find $1 -type f -not -path "./ts_xml/*" -not -path "./grepper/*" -name '*.ipynb'     -exec grep -l SALPY_$2 {} \; >> refs/$2
find $1 -type f -not -path "./ts_xml/*" -not -path "./grepper/*" -name '*.py'        -exec grep -l "from lsst.ts.$2" {} \; > refs/$2.pyimport
find $1 -type f -not -path "./ts_xml/*" -not -path "./grepper/*" -name '*.vi'        -exec grep -l SALLV_$2 {} \; >> refs/$2
find $1 -type f -not -path "./ts_xml/*" -not -path "./grepper/*" -name '*.cpp'       -exec grep -l "SAL_$2.h" {} \; >> refs/$2
find $1 -type f -not -path "./ts_xml/*" -not -path "./grepper/*" -name '*.h'         -exec grep -l "SAL_$2.h" {} \; >> refs/$2
find $1 -type f -not -path "./ts_xml/*" -not -path "./grepper/*" -name '*.java'      -exec grep -l "org.lsst.sal.SAL_$2" {} \; >> refs/$2
find $1 -type f -not -path "./ts_xml/*" -not -path "./grepper/*" -name '*.sal'       -exec grep -l "org.lsst.sal.SAL_$2" {} \; >> refs/$2
find $1 -type f -not -path "./ts_xml/*" -not -path "./grepper/*" -name '*.yaml'      -exec grep -l "device: $2" {} \; >> refs/$2
find $1 -type f -not -path "./ts_xml/*" -not -path "./grepper/*" -name 'Jenkinsfile' -exec grep -l " $2 " {} \; >> refs/$2
find $1 -type f -not -path "./ts_xml/*" -not -path "./grepper/*" -name '*.js'        -exec grep -l "name: '$2'" {} \; >> refs/$2
echo "find $1 -type f -name '*.py'       -exec grep -l 'salobj.Remote.*$2' {} \; >> refs/$2" > /tmp/doit
echo "find $1 -type f -name '*.py'       -exec grep -l 'salobj.Controller.*$2' {} \; >> refs/$2" >> /tmp/doit
echo "find $1 -type f -name '*.jsx'      -exec grep -l '\\-$2\\-' {} \; >> refs/$2" >> /tmp/doit
echo "find $1 -type f -name 'Dockerfile' -exec grep -l '$2\\-' {} \; >> refs/$2" >> /tmp/doit
chmod 755 /tmp/doit
/tmp/doit

