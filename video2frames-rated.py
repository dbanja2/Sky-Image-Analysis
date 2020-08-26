# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:06:43 2019
@author: dbanja2
"""

import cv2
import numpy as np
import os
import math

# Playing video from file:
cap = cv2.VideoCapture('20131201_northlapse.mov')
frameRate = cap.get(5)  #frame rate is 1 per second

try:
    if not os.path.exists('N131201'):
        os.makedirs('N131201')
except OSError:
    print ('Error: Creating directory of data')

#currentFrame = 0
while(True):
    # Capture frame-by-frame
    frameId = cap.get(1)  #current frame nnumber
    ret, frame = cap.read()
    if (ret != True):
        break
    # Saves image of the current frame in jpg file
    #name = './N130101/130101N_' + str(currentFrame) + '.jpg'
    if (frameId % math.floor(frameRate) == 0):
        name = './N131201/131201N_' + str(frameId) + '.jpg'
        print ('Creating...' + name)
        cv2.imwrite(name, frame)

    # To stop duplicate images
    #currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()