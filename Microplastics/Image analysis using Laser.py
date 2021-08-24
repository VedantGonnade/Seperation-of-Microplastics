# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 09:16:52 2021

@author: ritasha
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import cv2
import glob
import pandas as pd
from xlwt.Workbook import *
from pandas import ExcelWriter
import xlsxwriter  



labels=['PET','HDPE','PS','PP','PC','PA','LDPE','PVC','E. cordatum','H. trunculus','S. officinalis','N. josephina','P. oceanica','wood with teredo','cellulose','sand'] 
Colors=['blue','green','black','red','orange','violet','grey','yellow','red','yellow','grey','green','orange','black','blue','violet']


Exp='Brett'
folderpath1='C:/Users/ritasha/Desktop/Srumika/PHD/gonnade/29.04 measurements'



ref=cv2.imread('C:/Users/ritasha/Desktop/Srumika/PHD/gonnade'+'/RUV_set_2_ref_4.png')


bg=cv2.imread(folderpath1+'/NPset2 bg_500ms_1.png')
#bg=bg.flatten()
bg1=cv2.imread(folderpath1+'/NPset4 bg_500ms_1.png')
#bg1=bg1.flatten()
bg2=cv2.imread(folderpath1+'/NPset6 bg_500ms_1.png')
#bg2=bg2.flatten()



filt=['420','440','460','500','560']

n=0
lm=-1
name='/Pset'
Allsets1=[[[]for _ in range(8)] for _ in range(len(filt))]
Allsets=[[[]for _ in range(8)] for _ in range(len(filt))]
Allsetsfiles1=[[[]for _ in range(8)] for _ in range(len(filt))]
for i in range(1,9): #sets
    if i%2 ==0:
        m=4+n
        n=n+1
        name='/NPset'
    else:
        m=lm+1
        lm=lm+1
        name='/Pset'
    for j in range(len(filt)): # filters
        if i==3:
            lmn=' '
        else:
            lmn=' F'
        filters=glob.glob(folderpath1+name+str(i)+lmn+filt[j]+'_*')
        for k in range(len(filters)):
            imgdata1=cv2.imread(filters[k])
            imgdata=np.subtract(imgdata1.astype(np.int16),bg.astype(np.int16))
            Allsets1[j][m].append(imgdata) 
            Allsets[j][m].append(imgdata1) 
        Allsetsfiles1[j][m].append(filters) 

        
   
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
        
def subsampling(x):
    value=5
    l=0
    x=7
    image=Allsets[l][x][5]
    Cont = [] 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gray,value, 255, cv2.THRESH_BINARY )
    thresh = cv2.erode(thresh, np.ones((5,5)))
    cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
    (cnts, boundingBoxes) = sort_contours(cnts, method="right-to-left")
        
    for (j, c) in enumerate(cnts):
        if cv2.contourArea(c) > 2200:
            Cont.append(c)
            #uncomment to check contouring
            # mask = np.zeros_like(gray)
            # cv2.drawContours(mask,[c],-1, 255, -1)
            # res = cv2.bitwise_and(image,image,mask=mask)
            # res = cv2.resize(res, (960, 540))
            # cv2.imshow('res', res)
            # cv2.waitKey(0)
    return Cont


Samples1=[[[]for _ in range(16)] for _ in range(5)] #all filters
op=0
for l in range(len(Allsets1)):# filters
    for i in range(len(Allsets1[l])): #### sets
        for j in range(len(Allsets1[l][i])):  #### repetition
            Z = Allsets[l][i][j]
            Cont=subsampling(i) #making contours based on 370 nm filter

            for k in range(0, len(Cont)): # no.of samples

                x,y,w,h = cv2.boundingRect(Cont[k])
                ROI = Z[y:y+h, x:x+w]
                chanels = [blue, green, red] = ROI[:,:,0], ROI[:,:,1], ROI[:,:,2]
                colarr=[blue, green, red] = blue.flatten(), green.flatten(), red.flatten()
        
                Zscore=[Zscore1,Zscore2,Zscore3]=stats.zscore(blue),stats.zscore(green),stats.zscore(red)
                p=0
                channels=[]
                for m in range(3): #to take and average of 3 colors
                    a = np.argwhere(Zscore[m]>(np.min(Zscore[m])+0.5))
                    b=np.argwhere(Zscore[m]<(np.quantile(Zscore[m],0.98)))
                        
                    c= np.intersect1d(a,b)
                    if np.size(c)==0:
                          new_blue=colarr[m]
                    else:
                        new_blue=colarr[m][c] 
                    #new_blue=colarr[m]
                    chan=np.mean(new_blue)
                    channels.append(chan)
                
                if l==0: 
                    colorcombo=[channels]
                else:
                    if l==4:
                        p=1
                    colorcombo = channels[p]+channels[p+1]
                if k<=2:
                    op=i+i
                else:
                    op=i+i+1
                Samples1[l][op].append(colorcombo) # i indicates filters
                #SamplesSTD[i][k].append(STD)

folderpath='C:/Users/ritasha/Desktop/Srumika/PHD/gonnade/Results/laser_29.04 with diffuser'



fig = plt.figure(figsize=(6,6)) 
ax = plt

for i in range(16): #samples
    for j in range(15): #repetions, replicates
        X=Samples1[0][i][j]
        if i==15 and j==9:
            break
        if i<8:
            s='s'
        else:
            s='*'
        ax.scatter(X[0][0]/X[0][1],X[0][1]/X[0][2],marker=s,s=50,color=Colors[i])
    ax.scatter(X[0][0]/X[0][1],X[0][1]/X[0][2],marker=s,s=50,label=labels[i],color=Colors[i])    
    plt.axvline(x=1.48,c='grey',ls='-.')
    ax.xlabel('Blue/ Green channel',fontsize=16)
    ax.ylabel('Green/ Red channel',fontsize=16)
    ax.tick_params(axis='both',direction="in", which='major', labelsize=12)
    #ax.set_zlabel('Red channel')
    ax.xlim(0.75,2.6)
    ax.ylim(1.1,2.1)

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10),ncol=4,fontsize=16)

plt.savefig(folderpath+'/diffused laser_RGB',dpi=1000, transparent=False, papertype=None,bbox_inches='tight')


fig = plt.figure(figsize=(6,6)) 
ax = plt

for i in range(16):
    for j in range(len(Samples1[1][i])):
        if i<8:
            s='s'
        else:
            s='*'
        plt.scatter(Samples1[2][i][j]/Samples1[3][i][j],Samples1[1][i][j]/Samples1[4][i][j],marker=s,s=50,color=Colors[i])
    plt.scatter(Samples1[2][i][j]/Samples1[3][i][j],Samples1[1][i][j]/Samples1[4][i][j],marker=s,s=50,color=Colors[i],label=labels[i])
    plt.axvline(x=0.9,c='grey',ls='-.')
    ax.xlabel('Parameter P1',fontsize=16)
    ax.ylabel('Parameter P2',fontsize=16)
    ax.tick_params(axis='both',direction="in", which='major', labelsize=12)

    #ax.set_zlabel('Red channel')
    # ax.xlim(0,7.5)
    # ax.ylim(0,2.75)

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10),ncol=4,fontsize=16)


plt.savefig(folderpath+'/diffused laser_MF.png',dpi=1000, transparent=False, papertype=None,bbox_inches='tight')


fig = plt.figure(figsize=(1,3)) 
ax = plt

K=[7,8,11]

Labels=['PVC', 'E. cordatum', 'N. josephina']
Pos=[1,2,3]

for l in range(3):
    i=K[l]
    for j in range(len(Samples1[1][i])):
        if i<8:
            s='s'
        else:
            s='*'
        plt.scatter(1,Samples1[1][i][j],marker=s,s=50,color=Colors[i])
    plt.scatter(1,Samples1[1][i][j],marker=s,s=50,color=Colors[i],label=labels[i])
    #plt.axvline(x=0.9,c='grey',ls='-.')
    #ax.xlabel('Pixel counts F440',fontsize=16)
    ax.xticks([])
    ax.yticks([15,45,75])
    ax.ylabel('Pixel counts BPF-440nm ± 10 nm',fontsize=8)
    ax.tick_params(axis='both',direction="in", which='major', labelsize=10)

    #ax.set_zlabel('Red channel')
    # ax.xlim(0,7.5)
    # ax.ylim(0,2.75)
plt.savefig(folderpath+'/laser_440.png',dpi=1000, transparent=False, papertype=None,bbox_inches='tight')



#plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.10),ncol=4,fontsize=16)
