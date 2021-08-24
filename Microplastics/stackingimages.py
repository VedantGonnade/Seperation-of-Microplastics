# -*- coding: utf-8 -*-
"""
Created on Tue Feb  9 14:15:17 2021

@author: Admin
"""
import cv2
import numpy as np


def stackImages(scale, imgArray):
    rows = len(imgArray)
    colms = len(imgArray[0])
    rowsAvailable = isinstance(imgArray[0], list)
    width = imgArray[0][0].shape[0]
    height = imgArray[0][0].shape[0]
    
    if rowsAvailable:
        for x in range(0, rows):
            for y in range(0, colms):
                if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
                else:
                    imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
                if len(imgArray[x][y].shape) == 2:
                    imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
                    
            imageBlank = np.zeros((height, width), np.uint8)
            hor = [imageBlank]*rows
            hor_con = [imageBlank]*rows
            for x in range(0, rows):
                hor[x] = np.hstack(imgArray[x])
            ver = np.vstack(hor)
            
    else:
        for x in range(0, rows):
            if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
                imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale,scale)
            else:
                imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale,scale)
            if len(imgArray[x].shape) == 2:
                imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
                
        hor = np.hstack(imgArray)
        ver = hor
        
    return ver


                
img1 = cv2.imread('F:\Multispectral Imaging\Readings\Reading to find intensity of two samples in one image\image0.bmp', -1)
img2 = cv2.imread('F:\Multispectral Imaging\Readings\Reading to find intensity of two samples in one image\image1.bmp', -1)
img3 = cv2.imread('F:\Multispectral Imaging\Readings\Reading to find intensity of two samples in one image\image2.bmp', -1)
img4 = cv2.imread('F:\Multispectral Imaging\Readings\Reading to find intensity of two samples in one image\image3.bmp', -1)
#img5 = cv2.imread('F:\Multispectral Imaging\Readings\Reading to find intensity of two samples in one image\image4.bmp', -1)
# print(img1.shape)

# width = int(img1.shape[1] * 50 / 100)
# height = int(img1.shape[0] * 50/ 100)
# dim = (width, height)

# img11 = cv2.resize(img1,dim, interpolation = cv2.INTER_AREA)
# img21 = cv2.resize(img2,dim, interpolation = cv2.INTER_AREA)
# img31 = cv2.resize(img3,dim, interpolation = cv2.INTER_AREA)
# img41 = cv2.resize(img4,dim, interpolation = cv2.INTER_AREA)

# print(img11.shape)

# hor = np.hstack((img11, img21))
# ver = np.vstack((img31, img41))

stackedImages = stackImages(0.3, ([img1,img1, img1,img1]))



cv2.imshow('stack_images', stackedImages)





#cv2.imshow('her', hor)
#cv2.imshow('ver', ver)
cv2.waitKey(0)








