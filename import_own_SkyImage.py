#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Apr 16, 2018 
@author: dbanja2
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import cv2
import random # to shuffle our training data
import pickle

DATADIR = "C:/Users/dbanja2/Downloads/SkyImages"
CATEGORIES = ["Cloudy", "OverCast", "Sunny"] 
#index value is 0, 1 and 2 for cloudy, overcast and sunny
for category  in CATEGORIES:
    path = os.path.join(DATADIR, category)  
    #paths to cloudy, overcast or sunny directory
    for img in os.listdir(path):
        #cv2.IMREAD_GRAYSCALE makes the image grayscale
        #img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
        img_array = cv2.imread(os.path.join(path,img))
        #plt.imshow(img_array, cmap="gray")
        plt.imshow(img_array)
        plt.show()
        break
    break
#print(img_array.shape)
#print(img_array)  #prints the image array
IMG_SIZE = 300   #change this number to change pixel size&clarity
new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
#plt.imshow(new_array, cmap = 'gray')
#plt.show()

#----to revert back to RGB from BGR-----
#plt.imshow(cv2.cvtColor(new_array, cv2.COLOR_BGR2RGB))
#plt.show()


training_data = []
def create_training_data():
    for category  in CATEGORIES:
        path = os.path.join(DATADIR, category)  #paths to cloudy, overcast or sunny directory
        class_num = CATEGORIES.index(category) #assign cloudy, overcast or sunny category as 0 , 1 and 2
        for img in os.listdir(path):
            try:    #cv2.IMREAD_GRAYSCALE makes the image grayscale or cv2.IMREAD_COLOR
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
                training_data.append([new_array, class_num])
            except Exception as e:
                pass
              
#run the create training data function
create_training_data()
print(len(training_data))
random.shuffle(training_data)
#for sample in training_data[:10]: #taking data upto 10 for now
   # print (sample[1])

XS = [] #X is generally a feature set
yS = [] # y is generally labels

for features, label in training_data:
    XS.append(features)
    yS.append(label)

#X has to be a numpy array, in reshape(); -1 implies how many features(it is arbitrary now)
# and shape of the data to be of IMG_SIZE then 1 for grayscale/ remove
# 1 it to work with color image
#X = np.array(X).reshape(-1, IMG_SIZE, IMG_SIZE, 1)
XS = np.array(XS).reshape(-1, IMG_SIZE, IMG_SIZE, 1)

#to save files(we can use module other than pickle too)
pickle_out = open("XS.pickle", "wb")
pickle.dump(XS, pickle_out)
pickle_out.close()

pickle_out = open("yS.pickle", "wb")
pickle.dump(yS, pickle_out)
pickle_out.close()

#later if we nee to open
#pickle_in = open("X.pickle", rb)
#X[1]   3 to see our X array



