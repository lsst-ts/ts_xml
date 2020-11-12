#!/bin/sh

pkgs="aoclcSim astrosky ataos ATHexapod atspectrograph ATTCS ATWhiteLightSource cbp dateloc dimm dsm electrometer externalscripts FiberSpectrograph GenericCamera idl laser linearstage monochromator mtdome mteec observatory ofc phosim proposalScheduler pythonCommunicator pythonFileReader pythonFitsfile rotator salobj salpytools schedulerConfig scheduler scriptqueue standardscripts statemachine tunablelaser watcher wep WeatherStation"
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
