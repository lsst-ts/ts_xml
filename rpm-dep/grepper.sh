#!/bin/sh
mkdir -p grepper
echo "Getting list of repositories"
curl "https://api.github.com/users/lsst-ts/repos?page=1&per_page=100" | grep clone_url > grepper/tsrepos1
curl "https://api.github.com/users/lsst-ts/repos?page=2&per_page=100" | grep clone_url > grepper/tsrepos2
curl "https://api.github.com/users/lsst-ts/repos?page=3&per_page=100" | grep clone_url > grepper/tsrepos3
curl "https://api.github.com/users/lsst-ts/repos?page=4&per_page=100" | grep clone_url > grepper/tsrepos4
cat grepper/tsrepos1 grepper/tsrepos2 grepper/tsrepos3 grepper/tsrepos4 > grepper/tsrepos
perl -pi -w -e 's/    \"clone_url\": \"/git clone /g;' grepper/tsrepos
perl -pi -w -e 's/\",//g;' grepper/tsrepos
chmod 755 grepper/tsrepos

echo "Cloning lsst-ts and lsst-dm repositories"
./grepper/tsrepos
if [ ! -z "$1" ]; then 
  ./tsprivate.rpm-dep $1
fi
./dmrepos.rpm-dep

echo "Fetching CCS assets"
mkdir ccs
cd ccs
curl -L -o org-lsst-sal-atcamera-source.jar  "http://repo-nexus.lsst.org/nexus/service/rest/v1/search/assets/download?sort=version&direction=desc&repository=ccs-maven2-public&maven.groupId=org.lsst&maven.artifactId=org-lsst-sal-atcamera&maven.classifier=sources&maven.extension=jar"
curl -L -o org-lsst-sal-camera-source.jar  "http://repo-nexus.lsst.org/nexus/service/rest/v1/search/assets/download?sort=version&direction=desc&repository=ccs-maven2-public&maven.groupId=org.lsst&maven.artifactId=org-lsst-sal-camera&maven.classifier=sources&maven.extension=jar"
#curl -L -o org-lsst-sal-cccamera-source.jar  "http://repo-nexus.lsst.org/nexus/service/rest/v1/search/assets/download?sort=version&direction=desc&repository=ccs-maven2-public&maven.groupId=org.lsst&maven.artifactId=org-lsst-sal-cccamera&maven.classifier=sources&maven.extension=jar"
curl -L -o org-lsst-sal-codegen-source.jar  "http://repo-nexus.lsst.org/nexus/service/rest/v1/search/assets/download?sort=version&direction=desc&repository=ccs-maven2-public&maven.groupId=org.lsst&maven.artifactId=org-lsst-sal-codegen&maven.classifier=sources&maven.extension=jar"
curl -L -o org-lsst-sal-core-source.jar  "http://repo-nexus.lsst.org/nexus/service/rest/v1/search/assets/download?sort=version&direction=desc&repository=ccs-maven2-public&maven.groupId=org.lsst&maven.artifactId=org-lsst-sal-core&maven.classifier=sources&maven.extension=jar"
jar xvf org-lsst-sal-atcamera-source.jar
jar xvf org-lsst-sal-camera-source.jar
#jar xvf org-lsst-sal-cccamera-source.jar
jar xvf org-lsst-sal-codegen-source.jar
jar xvf org-lsst-sal-core-source.jar
rm *.jar
cd ..

echo "Prescan tidyup"
rm -fr bh errorcodes */.git opsim4_config ts_uml* ocs_xml ts_sal ts_sal_runtime ts_opensplice sal_topics_website robotframework*
rm -fr common* Common* explorations_*
find . -type f -name '*.lv*' -exec rm {} \;
find . -type f -name '*.fits' -exec rm {} \;

rm -fr refs
mkdir refs
grep "<Name>" ts_xml/sal_interfaces/SALSubsystems.xml > csclist
perl -pi -w -e 's/  <Name>//g;' csclist
perl -pi -w -e 's/<\/Name>//g;' csclist
cscs=`cat csclist`

for csc in $cscs
do
   echo "Grepping for $csc"
   ./dogrep.sh . $csc
done

repos=`ls`
cd refs
for repo in $repos
do
   echo "Building deps for $repo"
   grep -l $repo * > $repo.deps
done
find . -name '*.deps' -empty -exec rm {} \;

