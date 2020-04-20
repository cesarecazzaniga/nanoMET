#!/bin/bash

#
# Example of usage:
# submitCondor.py --execFile condor.sh --queue tomorrow postProcessed.sh
#

export USER=$(whoami)
initial="$(echo $USER | head -c 1)"
export SCRAM_ARCH=slc7_amd64_gcc700

echo "---------------------"
echo "Grid certificate 1"
voms-proxy-info --all
echo "---------------------"
echo "Current dir: `pwd`"
ls -l
echo "---------------------"
export HOME=/afs/cern.ch/user/${initial}/${USER}
echo "Current home dir: ${HOME}"
echo "---------------------"

echo "---------------------"
echo "Changing to script dir: $IWD"
cd $IWD
ls -l
echo "---------------------"

eval `scramv1 runtime -sh`

echo "Executing:"
echo ${@:2}
echo "---------------------"

${@:2}
