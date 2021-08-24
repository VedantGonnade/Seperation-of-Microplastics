# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 13:31:19 2020

@author: Vedant Gonnade
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('F:\Multispectral Imaging\Readings\Different images while studying openCV\Threshold images\on-Plastics\Officinalis\Officinalis 610 nm\with 610 nm filter.bmp', -1)
#print(img1)
cv2.imshow('img', img)

ret,thresh1 =  cv2.threshold(img,127,255,cv2.THRESH_BINARY)

cv2.imwrite('Binary Filter.bmp', thresh1)
count = cv2.countNonZero(thresh1)
print('non zero count:',count)

print('mean:',np.mean(img))
cv2.waitKey(0)
cv2.destroyAllWindows()