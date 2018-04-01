#!/bin/bash
pushd `dirname $0` > /dev/null
SCRIPTPATH=`pwd -P`

echo $SCRIPTPATH

python photobooth.py --printhook=./print-hook.py
