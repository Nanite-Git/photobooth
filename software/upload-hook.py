#!/usr/bin/env python

import sys
import cups
import time
import os

from subprocess import call

todays_dir = time.strftime("%Y-%m-%d")
pic_name = time.strftime("%Y-%m-%d %H-%M-%S.jpg")

output_file = "~/photo-ouput/" + todays_dir + "/" + pic_name +  ".jpg"

np = len(sys.argv) -1

if np < 1:
    print 'Not enough arguments'
    quit()


if np == 4:

    if not os.path.exists(os.path.dirname(output_file)):
        os.makedirs(os.path.dirname(output_file))
    #print sys.argv

    #call(["montage", sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], "-tile", "2x2", "-geometry" ,"1824x1232+20+20", "tile_4.jpg"])
    #call(["montage", sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], "-tile", "2x2", "-geometry" ,"1804x1232+20+20", "tile_4.jpg"])
    call(["montage", sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], "-tile", "2x2", "-geometry" ,"1804x1232+20+20", output_file])
    #print "Finished"
