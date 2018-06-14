#!/bin/bash

sudo apt-get install usbmount -y
sudo apt-get install ntfs-3g -y

sed -i 's/FILESYSTEMS=/FILESYSTEMS=\"vfat ntfs fuseblk ext2 ext3 ext4 hfsplus\"/g' /etc/usbmount/usbmount.conf
sed -i 's/FS_MOUNTOPTIONS=/FS_MOUNTOPTIONS=\"-fstype=ntfs-3g,nls=utf8,umask=007,gid=46-fstype=fuseblk,nls=utf8,umask=007,gid=46 -fstype=vfat,gid=1000,uid=1000,umask=007\"/g' /etc/usbmount/usbmount.conf


sudo apt install python-pip -y

sudo pip install qrcode
sudo pip install pyocclient