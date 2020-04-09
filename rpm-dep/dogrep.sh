#!/bin/sh
#
# dogrep.sh source_directory CSC
#
# e.g.
#   dogrep.sh at_ataos ATMCS
#
if false; then
    grep_opts="$grep_opts -l"
fi

function do_grep
{
    grep $grep_opts -r -E --exclude-dir=.git --exclude-dir=grepper --exclude-dir=ts_xml "$@"
}

do_grep --include='*.vi'                          -e "SALLV_$2"               $1
do_grep --include='*.cpp'  --include='*.h'        -e "SAL_$2.h"               $1
do_grep --include='*.java' --include='*.sal'      -e "org.lsst.sal.SAL_$2"    $1
do_grep --include='*.js'                          -e "name: '$2'"             $1
do_grep --include='*.jsx'                         -e "\-$2\-"                 $1
do_grep --include='Jenkinsfile'                   -e " $2 "                   $1
do_grep --include='Dockerfile'                    -e "$2\-"                   $1
do_grep --include='*.yaml'                        -e "^[^#]*\<device: $2"     $1

do_grep --include=*.py --include=*.ipynb \
	-e "SALPY_$2" \
	-e "super\(\)\.__init__\( *['\"]$2['\"] *," \
	-e "Controller\( *['\"]$2['\"] *\)" \
	-e "Remote\( *[^,]+, *['\"]$2['\"].*\)"                               $1

