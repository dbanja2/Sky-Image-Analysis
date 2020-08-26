# -*- coding: utf-8 -*-
"""
This code section will test the sky images and
print the prediction accuracy for the given image
category, eg. cloudy, overcast or sunny.
@author: dbanja2
"""

import cv2
import tensorflow as tf

CATEGORIES = ["Cloudy", "OverCast", "Sunny"]

def prepare(filepath):
    IMG_SIZE = 300
    img_array = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
    new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)

model = tf.keras.models.load_model("ConvulationNN_SkyImage.py")

#predict against a list of images 
prediction = model.predict(['131101N_460.jpg'])
print(prediction)
