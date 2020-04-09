#!/bin/sh

out_dir="refs-all"

if false; then

mkdir -p grepper

if true; then
    echo Skipping retrieving code
else

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
  tsprivate.rpm-dep $1
fi
dmrepos.rpm-dep

echo "Fetching CCS assets"
mkdir ccs
cd ccs
curl -L -o org-lsst-sal-atcamera-source.jar  "http://repo-nexus.lsst.org/nexus/service/rest/v1/search/assets/download?sort=version&direction=desc&repository=ccs-maven2-public&maven.groupId=org.lsst&maven.artifactId=org-lsst-sal-atcamera&maven.classifier=sources&maven.extension=jar"
curl -L -o org-lsst-sal-camera-source.jar  "http://repo-nexus.lsst.org/nexus/service/rest/v1/search/assets/download?sort=version&direction=desc&repository=ccs-maven2-public&maven.groupId=org.lsst&maven.artifactId=org-lsst-sal-camera&maven.classifier=sources&maven.extension=jar"
#curl -L -o org-lsst-sal-cccamera-source.jar  "http://repo-nexus.lsst.org/nexus/service/rest/v1/search/assets/download?sort=version&direction=desc&repository=ccs-maven2-public&maven.groupId=org.lsst&maven.artifactId=org-lsst-sal-cccamera&maven.classifier=sources&maven.extension=jar"
curl -L -o org-lsst-sal-codegen-source.jar  "http://repo-nexus.lsst.org/nexus/service/rest/v1/search/assets/download?sort=version&direction=desc&repository=ccs-maven2-public&maven.groupId=org.lsst&maven.artifactId=org-lsst-sal-codegen&maven.classifier=sources&maven.extension=jar"
curl -L -o org-lsst-sal-core-source.jar  "http://repo-nexus.lsst.org/nexus/service/rest/v1/search/assets/download?sort=version&direction=desc&repository=ccs-maven2-public&maven.groupId=org.lsst&maven.artifactId=org-lsst-sal-core&maven.classifier=sources&maven.extension=jar"

if true; then
    jar="unzip"
else
    jar="jar xvf"
fi

$jar xvf org-lsst-sal-atcamera-source.jar
$jar xvf org-lsst-sal-camera-source.jar
#$jar xvf org-lsst-sal-cccamera-source.jar
$jar xvf org-lsst-sal-codegen-source.jar
$jar xvf org-lsst-sal-core-source.jar

rm *.jar
cd ..

fi

echo "Prescan tidyup"
rm -fr bh errorcodes opsim4_config ts_uml* ocs_xml ts_sal ts_sal_runtime ts_opensplice sal_topics_website robotframework*
rm -fr common* Common* explorations_*
find . -type f -name '*.lv*' -exec rm {} \;
find . -type f -name '*.fits' -exec rm {} \;

fi

rm -fr $out_dir
mkdir $out_dir
grep "<Name>" ts_xml/sal_interfaces/SALSubsystems.xml > csclist
perl -pi -w -e 's/  <Name>//g;' -e 's/<\/Name>//g;' csclist
cscs=$(cat csclist)

for csc in $cscs
do
   echo "Grepping for $csc"
   dogrep.sh . $csc > $out_dir/$csc
done

repos=$(ls)
for repo in $repos; do
   #echo "Building deps for $repo"
   grep -r -E -l "\<$repo\>" --exclude=*.deps $out_dir | perl -pe "s|$out_dir/||" > $out_dir/$repo.deps
done

# HeaderService is called {AT,CC,MT}HeaderService in ts_xml
for hs in {AT,CC,MT}HeaderService; do
    cp $out_dir/HeaderService.deps $out_dir/$hs.deps
done
rm $out_dir/HeaderService.deps

find $out_dir -name '*.deps' -empty -exec rm {} \;
