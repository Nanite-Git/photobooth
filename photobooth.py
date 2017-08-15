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


directory = 'output' 
number_of_picture = 4
textcolor = (150,250,150)
shadowcolor = (60,60,60)

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
    img = pygame.Surface(size, 16)
    
    #img = pygame.Surface(size, pygame.SRCALPHA,32)
    #img = img.convert_alpha()
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

print dispx, dispy

screen = pygame.display.set_mode((dispx,dispy), pygame.FULLSCREEN)
BackGround = Background('gray-slate-background.jpg', [0,0])

screen.fill([255, 255, 255])
screen.blit(BackGround.image, BackGround.rect)
pygame.display.update()

myfont = pygame.font.SysFont('Droid Sans Mono', 120)
pygame.mouse.set_visible(0)

pygame.display.update()
time.sleep(3)


camera = picamera.PiCamera()
camera.vflip = True

pictures = []

def getFilename(prefix, number):
    return str(directory) + '/' + str(prefix) + '_' + str(number) + '.jpg'

def takePhotoSerie():
    global pictures
    pictures = []
    fileprefix = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    for i in range(4):
        pictures.append(takePicture(fileprefix, i))
    
    thank_you()
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

        #print 'Position ' + str(posx) + ' ' + str(posy)

        screen.blit(img, (posx, posy))

def takePicture(filename, file_number, wait_time = 10):
    textx = 1000
    texty = 220
    textcolor = (200,200,200)
    shadowcolor = (40,40,40)
    myfont = pygame.font.SysFont('Droid Sans Mono', 300)
    myfont_ready = pygame.font.SysFont('Droid Sans Mono', 120)

    

    if wait_time < 5:
        wait_time = 5

    for i in range(wait_time):
        screen.fill([255, 255, 255])
        screen.blit(BackGround.image, BackGround.rect)
        text_sh = myfont.render(str(10-i), False, shadowcolor)
        screen.blit(text_sh,(textx + 20, texty + 20))
        text_fg = myfont.render(str(10-i), False, textcolor)
        screen.blit(text_fg,(textx,texty))
        if i == (wait_time-5):
            camera.resolution = (640,480)
            camera.start_preview(fullscreen=False, window=(200,200,640,480))
        
        if i < (wait_time -3):
            text_sh = myfont_ready.render('get ready ...', False, shadowcolor)
            screen.blit(text_sh,(300 + 10, 800 + 10))
            text_fg = myfont_ready.render('get ready ...', False, textcolor)
            screen.blit(text_fg,(300,800))

        if file_number > 0:
            showPictures()

        pygame.display.update()
        pygame.time.wait(1000)
            
    camera.stop_preview()
    camera.resolution = (3280,2464)
    camera.capture(getFilename(filename, file_number))
    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)
    text_sh = myfont_ready.render('get ready ...', False, shadowcolor)
    screen.blit(text_sh,(300 + 10, 800 + 10))
    text_fg = myfont_ready.render('get ready ...', False, textcolor)
    screen.blit(text_fg,(300,800))
    pygame.display.update()

    os.path.isfile(getFilename(filename, file_number))
    
    photo_height = dispy/4
    #print photo_height
    photo_height = int(photo_height)
    img = pygame.image.load(getFilename(filename, file_number))
    isize = img.get_size()
    #print isize
    photo_width = (photo_height/isize[1])*isize[0]
    #print 'Photo_widht ' + str(photo_width)
    photo_width = int(photo_width)
    img = pygame.transform.scale(img, (photo_width, photo_height))
    return(img)
    

def thank_you():
    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)
    myfont = pygame.font.SysFont('Droid Sans Mono', 250)
    text_thankyou_sh = myfont.render('thank', False, shadowcolor)
    screen.blit(text_thankyou_sh,(50+20,200+20))
    text_thankyou = myfont.render('thank', False, textcolor)
    screen.blit(text_thankyou,(50,200))
    text_thankyou_sh = myfont.render('you!', False, shadowcolor)
    screen.blit(text_thankyou_sh,(300+20,500+20))
    text_thankyou = myfont.render('you!', False, textcolor)
    screen.blit(text_thankyou,(300,500))
    showPictures()
    pygame.display.update()


def start_screen():
    textcolor = (150,250,150)
    shadowcolor = (60,60,60)
    screen.fill([255, 255, 255])
    screen.blit(BackGround.image, BackGround.rect)
    text_start_sh = myfont.render('Press button to start!', False, shadowcolor)
    screen.blit(text_start_sh,(100+10,300+10))
    text_start = myfont.render('Press button to start!', False, textcolor)
    screen.blit(text_start,(100,300))
    pygame.display.update()



start_screen()
time.sleep(5)

takePhotoSerie()

time.sleep(5)

takePhotoSerie()

time.sleep(15)


