#!/bin/sh

echo "Prescan tidyup"
rm -fr refs
mkdir refs

if [ ! -d ts_xml ]; then
    git clone https://github.com/lsst-ts/ts_xml.git
fi
grep "<Name>" ts_xml/sal_interfaces/SALSubsystems.xml > csclist
perl -pi -w -e 's/  <Name>//g;' csclist
perl -pi -w -e 's/<\/Name>//g;' csclist
cscs=`cat csclist`

if false; then
    echo "   XXX RHL XXX Hack XXX" >&2
    cscs="ATAOS ATCamera ATHexapod ATMCS ATPneumatics Hexapod"
    #cscs="Hexapod"
fi

for csc in $cscs
do
    echo "Grepping for $csc"
    if true; then
	dogrep.sh $1 $csc > refs/$csc
    else
	dogrep-old.sh $1 $csc
    fi
done

cd refs
echo "Building deps for $1"
grep -l $1 * > $1.deps
echo "Dependencies for $1 are"
cat $1.deps
