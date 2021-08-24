# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 13:11:51 2020

@author: gonnade
"""
from pyueye import ueye
import ctypes

hCam = ueye.HIDS(1)
exitcamera = ueye.is_ExitCamera(hCam)

print(exitcamera)
if(exitcamera == ueye.IS_SUCCESS):
    print("Hurrey")