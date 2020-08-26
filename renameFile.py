# -*- coding: utf-8 -*-
"""
This code will rename any filename to list of numbers from 0
@author: dbanja2
"""

import os
os.getcwd()
collection = "C:/Users/username/yourSkyImagesLocation/SkyImages/Cloudy/"
for i, filename in enumerate(os.listdir(collection)):
    os.rename("C:/Users/username/yourSkyImagesLocation/SkyImages/Cloudy/" + filename, "C:/Users/username/yourSkyImagesLocation/SkyImages/Cloudy/" + str(i) + ".jpg")
