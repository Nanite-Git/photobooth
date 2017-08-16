# -*- coding: iso-8859-1 -*-
from __future__ import division
import pygame
import time
import picamera
import os, sys, pygame, pygame.font, pygame.image
from pygame.locals import *
import datetime
import os, errno
import os.path
import sys, getopt
import subprocess


directory = 'output' 
number_of_picture = 4
textcolor = (120,120,250)
shadowcolor = (30,30,30)
font = 'Droid Sans Mono'

###################################################################

printhook = ""
print_enabled = False

try:
    opts, args = getopt.getopt(sys.argv[1:],"",["printhook="])
except getopt.GetoptError:
        print 'photobooth.py --printhook <hookfile>'
        sys.exit(2)
for opt, arg in opts:
    if opt in ("--printhook"):
        printhook = arg
        print_enabled = True

try:
        os.makedirs(directory)
except OSError as e:
        if e.errno != errno.EEXIST:
                    raise

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def textDropShadow(font, message, offset, fontcolor, shadowcolor):
    base = font.render(message, 0, fontcolor)
    size = base.get_width() + offset, base.get_height() + offset
    img = pygame.Surface(size, pygame.SRCALPHA,32)
    img = img.convert_alpha()

    base.set_palette_at(1, shadowcolor)
    img.blit(base, (offset, offset))
    base.set_palette_at(1, fontcolor)
    img.blit(base, (0, 0))
    return img


pygame.init()
pygame.font.init()
infostuffs = pygame.display.Info() # gets monitor info

monitorx, monitory = infostuffs.current_w, infostuffs.current_h # puts monitor length and height into variables

dispx, dispy = 1920,1080

if dispx > monitorx: # scales screen down if too long
    dispy /= dispx / monitorx
    dispx = monitorx
if dispy > monitory: # scales screen down if too tall
    dispx /= dispy / monitory
    dispy = monitory

dispx = int(dispx) # So your resolution does not contain decimals
dispy = int(dispy)

dispx = monitorx
dispy = monitory

print dispx, dispy

screen = pygame.display.set_mode((dispx,dispy), pygame.FULLSCREEN)
BackGround = Background('gray-slate-background.jpg', [0,0])
BackGround = Background('background1.jpg', [0,0])
BackGround = Background('background2.png', [0,0])

screen.fill([255, 255, 255])
screen.blit(BackGround.image, BackGround.rect)
pygame.display.update()

bigfont = pygame.font.SysFont(font, 300)
smallfont = pygame.font.SysFont(font, 120)
pygame.mouse.set_visible(0)

pygame.display.update()
time.sleep(3)


camera = picamera.PiCamera()
camera.vflip = True

pictures = []
pic_preview_width = 10;

def getFilename(prefix, number):
    return str(directory) + '/' + str(prefix) + '_' + str(number) + '.jpg'

def takePhotoSerie():
    global pictures
    pictures = []
    fileprefix = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    for i in range(number_of_picture):
        pictures.append(takePicture(fileprefix, i))
    
    thank_you()


    if print_enabled:
        # Start printing
        # build hook call list
        hook = []
        hook.append(str(printhook))
        for i in range(number_of_picture):
            hook.append(str(getFilename(fileprefix, i)))
        subprocess.Popen(hook)

    pygame.time.wait(20000)
    start_screen()

def showPictures():
    photo_height = int(dispy / 4)
    for i in range(len(pictures)):
        img = pictures[i]
        isize = img.get_size()
        posx = dispx-isize[0]
        posy = i*photo_height

        posx = int(posx)
        posy = int(posy)

        screen.blit(img, (posx, posy))

def takePicture(filename, file_number, wait_time = 10):
    global pic_preview_width
    textx = ((dispx - 840)/2) + 840
    texty = 220

    if wait_time < 5:
        wait_time = 5
    
    camera.resolution = (640,480)
    camera.start_preview(fullscreen=False, window=(200,200,640,480))

    for i in range(wait_time):
        
        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)
        
        if file_number > 0:
            showPictures()

        c = textDropShadow(bigfont, str(10-i), 20, textcolor, shadowcolor)
        screen.blit(c, (textx-(c.get_size()[0]/2), texty))
        
        if i < (wait_time - 2):
            gr = textDropShadow(smallfont, 'get ready ...', 10, textcolor, shadowcolor)
            gr_rect = gr.get_size()
            screen.blit(gr, (int((dispx/2)-(gr_rect[0]/2)), 800))

        pygame.display.update()
        pygame.time.wait(1000)
            
    camera.stop_preview()
    camera.resolution = (3280,2464)
    camera.capture(getFilename(filename, file_number))
    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)
    if file_number > 0:
        showPictures()
    pygame.display.update()

    os.path.isfile(getFilename(filename, file_number))
    
    photo_height = dispy/4
    photo_height = int(photo_height)
    img = pygame.image.load(getFilename(filename, file_number))
    isize = img.get_size()
    photo_width = (photo_height/isize[1])*isize[0]
    photo_width = int(photo_width)
    pic_preview_width = photo_width
    img = pygame.transform.scale(img, (photo_width, photo_height))
    return(img)
    

def thank_you():
    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)
    t = textDropShadow(bigfont, 'thank', 20, textcolor, shadowcolor)
    screen.blit(t, (int(((dispx-pic_preview_width)/2)-(t.get_size()[0]/2)), 200))
    t = textDropShadow(bigfont, 'you', 20, textcolor, shadowcolor)
    screen.blit(t, (int(((dispx-pic_preview_width)/2)-(t.get_size()[0]/2)), 450))
    showPictures()
    pygame.display.update()


def start_screen():
    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)
    t = textDropShadow(smallfont, 'Press button', 10, textcolor, shadowcolor)
    screen.blit(t, (int((dispx/2)-(t.get_size()[0]/2)), int((dispy/2)-(t.get_size()[1])-75)))
    t = textDropShadow(smallfont, 'to start', 10, textcolor, shadowcolor)
    screen.blit(t, (int((dispx/2)-(t.get_size()[0]/2)), int((dispy/2)-(t.get_size()[1])+75)))
    pygame.display.update()


while 1:
    start_screen()
    pygame.time.wait(int(1000/25))
    event = pygame.event.poll()
    if event.type is pygame.KEYDOWN and ((event.key == pygame.K_RETURN) or (event.key == pygame.K_SPACE)):
        takePhotoSerie()
    
    if event.type is pygame.KEYDOWN and ((event.key == pygame.K_ESCAPE)):
        break







