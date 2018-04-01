#!/usr/bin/env python

import sys
import cups

from subprocess import call


output_file = "/dev/shm/tile.jpg"

np = len(sys.argv) -1

if np < 1:
    print 'Not enough arguments'
    quit()


if np == 4:

    #print sys.argv

    #call(["montage", sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], "-tile", "2x2", "-geometry" ,"1824x1232+20+20", "tile_4.jpg"])
    #call(["montage", sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], "-tile", "2x2", "-geometry" ,"1804x1232+20+20", "tile_4.jpg"])
    call(["montage", sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], "-tile", "2x2", "-geometry" ,"1804x1232+20+20", output_file])
    #print "Finished"
