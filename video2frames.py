# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 14:06:43 2019
@author: dbanja2
"""

import cv2
import numpy as np
import os

# Playing video from file:
cap = cv2.VideoCapture('20130101_northlapse.mov')
frameRate = cap.get(1)  #frame rate is 1 per second

try:
    if not os.path.exists('N130101'):
        os.makedirs('N130101')
except OSError:
    print ('Error: Creating directory of data')

currentFrame = 0
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    
      # Saves image of the current frame in jpg file
    name = './N130101/130101N_' + str(currentFrame) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # To stop duplicate images
    currentFrame += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()