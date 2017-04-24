

import cv2
import io
import numpy as np
import matplotlib.pyplot as plt
from picamera import PiCamera
from time import sleep
import time
from picamera.array import PiRGBArray
import serial
import unicodedata

ser = serial.Serial('/dev/ttyACM0',9600)

def match(a):
    good = []
    for m,n in a:
        if m.distance < 0.6*n.distance:
            good.append([m])
    
    if(len(good)>=5):
        return True
    else:
        return False
    
sums = 0
hun=0
five=0
twe=0
two=0
fif=0
ten=0
sift = cv2.xfeatures2d.SIFT_create()
base = 'base.jpg'
img1 = cv2.imread(base)
kpB, desB = sift.detectAndCompute(img1,None)

bf = cv2.BFMatcher()

img2000 = cv2.imread('two.jpg')
img500 = cv2.imread('five.jpg')
img10 = cv2.imread('ten1.jpg')
img50 = cv2.imread('fif.jpg')
img100 = cv2.imread('hun.jpg')
img20 = cv2.imread('twe.jpg')





kp2000, des2000 = sift.detectAndCompute(img2000,None)
kp500, des500 = sift.detectAndCompute(img500,None)
kp100, des100 = sift.detectAndCompute(img100,None)
kp10, des10 = sift.detectAndCompute(img10,None)
kp20, des20 = sift.detectAndCompute(img20,None)
kp50, des50 = sift.detectAndCompute(img50,None)
with PiCamera() as camera:
    camera.resolution = (640, 480)
    raw = PiRGBArray(camera, size=(640, 480))
    camera.framerate = 1.5
    raw.truncate(0)
    #sleep(2)
    #camera.capture(raw,format = 'bgr')
    for frame in camera.capture_continuous(raw,format = 'bgr',use_video_port = True):
        ser.write('A'.encode("utf-8"))
        #stream.truncate()
        #stream.seek(0)
        rawCapture = frame.array
        
        kpR, desR = sift.detectAndCompute(rawCapture,None)
        if(len(kpR)!= 0 ):
            matchesB = bf.knnMatch(desB,desR,k=2)
            matches100 = bf.knnMatch(des100,desR,k=2)
            matches500 = bf.knnMatch(des500,desR,k=2)
            matches10 = bf.knnMatch(des10,desR,k=2)
            matches20 = bf.knnMatch(des20,desR,k=2)
            matches50 = bf.knnMatch(des50,desR,k=2)
            matches2000 = bf.knnMatch(des2000,desR,k=2)
            if(match(matches100)):
                sums = sums+100
                hun+=1
            elif(match(matches500)):
                sums = sums+500
                five+=1
            elif(match(matches2000)):
                sums = sums+2000
                two+=1
            elif(match(matches20)):
                sums = sums+20
                twe+=1
            elif(match(matches10)):
                sums = sums+10
                ten+=1
            elif(match(matches50)):
                sums = sums+50
                fif+=1
            elif(match(matchesB)):
                
                break
        raw.truncate(0)
        print(1)
ser.flush()
ser.write('B'.encode("utf-8"));
ser.write(str(sums).encode("utf-8"))
print(sums,hun,five,ten,two,twe,fif)


