#!/usr/bin/env python

import sys
import cups
import time
import os
from datetime import datetime
from nextcloud_account import server, username, password

# pip install qrcode[pil]
import qrcode
#from qrcode.image.pure import PymagingImage

# pip install pyocclient
import owncloud

from subprocess import call

n = datetime.now()
folder_date = n
if folder_date.hour < 6:
    folder_date = datetime.today() - timedelta(days=1)



todays_dir = folder_date.strftime("%Y-%m-%d")
pic_name = n.strftime("%Y-%m-%d_%H-%M-%S.jpg")

output_file = "./photo-ouput/" + todays_dir + "/" + pic_name 
tmp_file = "/dev/shm/" + pic_name

np = len(sys.argv) -1


upload_dir = "photobooth/ " + todays_dir

def get_download_link():
    global upload_dir
    oc = owncloud.Client(server)
    oc.login(username, password)
    try:
        oc.mkdir("photobooth")
    except owncloud.HTTPResponseError:
       print "upload_dir already exists"

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
    return oc

def upload_file(filename):
    global upload_dir
    oc = get_download_link()

    success = False
    try:
        success = oc.put_file(upload_dir + "/" + os.path.basename(filename), filename)
    except owncloud.HTTPResponseError:
        print 'ERROR: Cannot Upload File'
        return False	
    
    return success

if np == 0:
    print 'Setup upload hook for today'
    get_download_link()
	

if np == 4:

    call(["montage", sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], "-tile", "2x2", "-geometry" ,"1804x1232+20+20", tmp_file])
    #call(["montage", sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], "-tile", "2x2", "-geometry" ,"2460x1846+20+20", "-quality", "75", tmp_file])
    #print "Finished"

    if upload_file(tmp_file):
        os.remove(tmp_file)
    else:
        if not os.path.exists(os.path.dirname(output_file)):
            os.makedirs(os.path.dirname(output_file))
        os.rename(tmp_file, output_file)
