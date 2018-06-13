#!/usr/bin/env python

import sys
import cups
import time
import os
from nextcloud_account import server, username, password

# pip install qrcode[pil]
import qrcode
#from qrcode.image.pure import PymagingImage

# pip install pyocclient
import owncloud

from subprocess import call

todays_dir = time.strftime("%Y-%m-%d")
pic_name = time.strftime("%Y-%m-%d %H-%M-%S.jpg")

output_file = "./photo-ouput/" + todays_dir + "/" + pic_name +  ".jpg"

np = len(sys.argv) -1


def upload_file(filename):
	oc = owncloud.Client(server)
	oc.login(username, password)
	upload_dir = time.strftime("%Y-%m-%d")
        try:
	    oc.mkdir(upload_dir)
        except owncloud.HTTPResponseError:
            print "upload_dir already exists"

	share_link = None
	if oc.is_shared(upload_dir):
		shares = oc.get_shares(upload_dir)
		
		for share in shares:
			link = share.get_link()
			if link is not None:
				share_link = link

	
	if share_link is None:
		link_info = oc.share_file_with_link(upload_dir, password="photobox")
		share_link = link_info.get_link()
		
	qr = qrcode.QRCode(
		version=1,
		error_correction=qrcode.constants.ERROR_CORRECT_L,
		box_size=10,
		border=4,
	)
	
	qr.add_data(share_link)
	qr.make(fit=True)

	img = qr.make_image(fill_color="black", back_color="white")
	image_file = open("/dev/shm/qr.png",'w+')
	img.save(image_file,"PNG")
	image_file.close() 
	
	oc.put_file(upload_dir + "/" + os.path.basename(filename), filename)
	
	

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

    upload_file(output_file)
