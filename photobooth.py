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
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)     # set up BCM GPIO numbering

button = 4
led_button = 5

led_red = 17
led_green = 6
led_blue = 27

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)    # set GPIO 25 as input
GPIO.setup(led_button, GPIO.OUT)
GPIO.setup(led_red, GPIO.OUT)
GPIO.setup(led_green, GPIO.OUT)
GPIO.setup(led_blue, GPIO.OUT)

directory = 'output' 
number_of_picture = 4
textcolor = (120,120,250)
shadowcolor = (30,30,30)
font = 'Droid Sans Mono'

usb_mount = "/media/usb0/"

###################################################################

printhook = ""
print_enabled = False

leds = (True, True, True)

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

def check_usb():
    global directory
    usb_dir = usb_mount + "/photobooth/output/"
    if os.path.ismount(usb_mount):
        if not os.path.exists(usb_dir):
            os.makedirs(usb_dir)

        directory = usb_dir


class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

def textDropShadow(font, message, offset, fontcolor, shadowcolor):
    base = font.render(message, False, fontcolor)
    size = base.get_width() + offset, base.get_height() + offset
    img = pygame.Surface(size, pygame.SRCALPHA,32)
    #img = img.convert_alpha()

    base.set_palette_at(1, shadowcolor)
    img.blit(base, (offset, offset))
    base.set_palette_at(1, fontcolor)
    #img.blit(base, (0, 0))
    img.blit(textOutline(font, message, fontcolor, (255,255,255)), (0, 0))
    #img.blit(textHollow(font, message, fontcolor), (0, 0))
    return img

def textHollow(font, message, fontcolor):
    notcolor = [c^0xFF for c in fontcolor]
    notcolor = (255,255,255)
    base = font.render(message, False, fontcolor)
    size = base.get_width() + 2, base.get_height() + 2
    img = pygame.Surface(size, pygame.SRCALPHA, 32)
    img = img.convert_alpha()
    base.set_colorkey(0)
    img.blit(base, (0, 0))
    img.blit(base, (2, 0))
    img.blit(base, (0, 2))
    img.blit(base, (2, 2))
    base.set_colorkey(0)
    base.set_palette_at(1, notcolor)
    img.blit(base, (1, 1))
    img.set_colorkey(notcolor)
    return img

def textOutline(font, message, fontcolor, outlinecolor):
    base = font.render(message, False, fontcolor)
    outline = textHollow(font, message, outlinecolor)
    img = pygame.Surface(outline.get_size(), pygame.SRCALPHA, 32)
    #img = img.convert_alpha()
    img.blit(outline, (0, 0))
    img.blit(base, (1, 1))
    img.set_colorkey(0)
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
#BackGround = Background('gray-slate-background.jpg', [0,0])
#BackGround = Background('background1.jpg', [0,0])
BackGround = Background('background2.png', [0,0])

screen.fill([255, 255, 255])
screen.blit(BackGround.image, BackGround.rect)
pygame.display.update()

bigfont = pygame.font.SysFont(font, 300)
smallfont = pygame.font.SysFont(font, 120)
pygame.mouse.set_visible(0)

pygame.display.update()
time.sleep(1)


camera = picamera.PiCamera()
camera.vflip = True

pictures = []
pic_preview_width = 10;


button_pressed = False;

def my_gpio_callback(channel):
    global button_pressed
    button_pressed = True

def getFilename(prefix, number):
    return str(directory) + '/' + str(prefix) + '_' + str(number) + '.jpg'

def takePhotoSerie():
    global pictures
    pictures = []
    fileprefix = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
    GPIO.output(led_button, False)
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

    pygame.time.wait(15000)
    GPIO.output(led_button, True)
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
        atime = pygame.time.get_ticks()
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
        btime = pygame.time.get_ticks()
        waittime = 1000-(btime-atime)
        if waittime <= 0:
            waittime = 1
        pygame.time.wait(waittime)
            
    camera.stop_preview()
    camera.resolution = (3280,2464)
    flash(True)
    camera.capture(getFilename(filename, file_number))
    flash(False)
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

def next_color():
    global leds
    if leds[0]:
        leds[0] = False
        leds[1] = True
    if leds[1]:
        leds[1] = False
        leds[2] = True
    if leds[2]:
        leds[2] = False
        leds[0] = True
    
    set_gpio_output()

def flash(status=True):
    global leds
    if status:
        leds = (True,True, True)
    else:
        leds = (False, False, False)
    
    set_gpio_output()

def set_gpio_output():
    GPIO.output(led_red, leds[0])
    GPIO.output(led_green, leds[1])
    GPIO.output(led_blue, leds[2])

GPIO.add_event_detect(button, GPIO.RISING, callback=my_gpio_callback)

start_screen()
counter = 0

check_usb()

while 1:
    event = pygame.event.poll()
    GPIO.output(led_button, True)
    if button_pressed or (event.type is pygame.KEYDOWN and ((event.key == pygame.K_RETURN) or (event.key == pygame.K_SPACE))):
        takePhotoSerie()
        start_screen()
        pygame.event.clear()
        button_pressed = False
    
    if event.type is pygame.KEYDOWN and ((event.key == pygame.K_ESCAPE)):
        pygame.quit()
        GPIO.cleanup()
        break

    pygame.time.wait(100)
    counter =+ 1

    if counter >= 10:
        counter = 0
        next_color()







