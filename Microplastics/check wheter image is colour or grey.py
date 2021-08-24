# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 14:20:07 2021

@author: Admin
"""
import cv2

img = cv2.imread('F:\Multispectral Imaging\Camera codes\Final codes\image0.bmp')
img1 = cv2.imread('F:\Multispectral Imaging\Readings\Reading on 17.02.2021 ( new camera)\PP, PS, PC\F500\image0.png', -1)
#print(img1.shape)

import cv2
def isgray(imgpath = 'F:\Multispectral Imaging\Camera codes\Final codes\h.png'):
    img = cv2.imread(imgpath)
    if len(img.shape) < 3: return True
    if img.shape[2]  == 1: return True
    b,g,r = img[:,:,0], img[:,:,1], img[:,:,2]
    if (b==g).all() and (b==r).all(): return True
    return False

print(isgray())
print(isgray('F:\Multispectral Imaging\Camera codes\Final codes\image0.png'))