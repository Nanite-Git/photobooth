#!/bin/bash
pushd `dirname $0` > /dev/null
SCRIPTPATH=`pwd -P`

echo $SCRIPTPATH

#python photobooth.py --printhook=./print-hook.py
python photobooth.py --printhook=./upload-hook.py
