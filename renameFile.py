# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 15:47:07 2019
This code will rename any filename to list of numbers from 0
@author: dbanja2
"""

import os
os.getcwd()
collection = "C:/Users/dbanja2/Downloads/SkyImages/Cloudy/"
for i, filename in enumerate(os.listdir(collection)):
    os.rename("C:/Users/dbanja2/Downloads/SkyImages/Cloudy/" + filename, "C:/Users/dbanja2/Downloads/SkyImages/Cloudy/" + str(i) + ".jpg")