#!/usr/bin/env python

import sys
import cups
import time

from subprocess import call


output_file = "/dev/shm/print-tile.jpg"

np = len(sys.argv) -1

if np < 1:
    print 'Not enough arguments'
    quit()


if np == 4:

    #call(["montage", sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], "-tile", "2x2", "-geometry" ,"1804x1232+20+20", output_file])
    call(["montage", sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], "-tile", "2x2", "-geometry" ,"2460x1846+20+20", output_file])
    #call(["montage", sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], "-tile", "2x2", "-geometry" ,"2460x1846", output_file])
    #print "Finished"
    conn = cups.Connection()
    printers = conn.getPrinters()
    printer_name = printers.keys()[0]
    printer_name = "Canon_CP1000"
    cups.setUser('pi')

    print printer_name

    print_id = conn.printFile(printer_name, output_file, "Photo Booth", {})
    # Wait until the job finishes
    while conn.getJobs().get(print_id, None):
        time.sleep(1)
        unlink(output_file)









