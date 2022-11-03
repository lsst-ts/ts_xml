#!/bin/sh

echo "Prescan tidyup"
rm -fr refs
mkdir refs

git clone https://github.com/lsst-ts/ts_xml.git
grep "<Name>" ts_xml/python/lsst/ts/xml/data/sal_interfaces/SALSubsystems.xml > csclist
perl -pi -w -e 's/  <Name>//g;' csclist
perl -pi -w -e 's/<\/Name>//g;' csclist
cscs=`cat csclist`

for csc in $cscs
do
   echo "Grepping for $csc"
   ./dogrep.sh $1 $csc
done

cd refs
echo "Building deps for $1"
grep -l $1 * > $1.deps
echo "Dependencies for $1 are"
cat $1.deps


