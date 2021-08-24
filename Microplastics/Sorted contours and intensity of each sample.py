# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 15:44:18 2021

@author: Admin
"""
import numpy as np
import cv2

def sort_contours(cnts, method="left-to-right"):
	# initialize the reverse flag and sort index
	reverse = False
	i = 0
	# handle if we need to sort in reverse
	if method == "right-to-left" or method == "bottom-to-top":
		reverse = True
	# handle if we are sorting against the y-coordinate rather than
	# the x-coordinate of the bounding box
	if method == "top-to-bottom" or method == "bottom-to-top":
		i = 1
	# construct the list of bounding boxes and sort them from top to
	# bottom
	boundingBoxes = [cv2.boundingRect(c) for c in cnts]
	(cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
		key=lambda b:b[1][i], reverse=reverse))
	# return the list of sorted contours and bounding boxes
	return (cnts, boundingBoxes)

image = cv2.imread("F:\Multispectral Imaging\Readings\Reading on 17.02.2021 ( new camera)\PP, PS, PC\F500\image0.png", -1)
image = cv2.resize(image, (960, 540))
accumEdged = np.zeros(image.shape[:2], dtype="uint8")
_,thresh = cv2.threshold(image,10, 255, cv2.THRESH_BINARY )
thresh = cv2.erode( thresh, np.ones((5,5)))

cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)

(cnts, boundingBoxes) = sort_contours(cnts, method="right-to-left")
# loop over the (now sorted) contours and draw them
for (i, c) in enumerate(cnts):
    if cv2.contourArea(c) > 20:
        mask = np.zeros_like(image)
        #draw_contour(mask, c, i)
        cv2.drawContours(mask,[c],-1, 255, -1)
        res = cv2.bitwise_and(image,image,mask=mask)
        
        row, col = (np.argmax(res)//res.shape[1],  np.argmax(res)%res.shape[1])
        
        row_min = row -1
        row_max = row +1
        col_min = col -1
        col_max = col +1
        Pix=image[row_min:row_max+1, col_min:col_max+1]
        
        MeanP=np.mean(Pix)
        print('Mean: ', MeanP)
        
        res = cv2.resize(res, (960, 540))
        
        #idx = np.where( mask==255)
        #print('mean:',np.mean(gray[idx]))
        #print('max:',np.max(gray[idx]))
        #cv2.imshow('original', image)
    
        cv2.imshow('object', res)
        cv2.waitKey(0)
        
    

cv2.destroyAllWindows()   



