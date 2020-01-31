#!/bin/sh

pkgs="aoclcSim astrosky ataos ATHexapod atspectrograph ATTCS ATWhiteLightSource cbp dateloc dimm dsm electrometer environment externalscripts FiberSpectrograph GenericCamera idl laser linearstage monochromator mteec observatory ofc phosim proposalScheduler pythonCommunicator pythonFileReader pythonFitsfile rotator salobj salpytools schedulerConfig scheduler scriptqueue standardscripts statemachine  tunablelaser watcher wep"
for pkg in $pkgs
do
  echo "Grepping for $pkg"
  find $1 -type f -name '*.py' -exec grep -l "from lsst.ts.$pkg" {} \; > pyrefs/$pkg
done

repos=`ls`
cd pyrefs
for repo in $repos
do
   echo "Building pydeps for $repo"
   grep -l $repo * > $repo.pydeps
done
find . -name '*.pydeps' -empty -exec rm {} \;
