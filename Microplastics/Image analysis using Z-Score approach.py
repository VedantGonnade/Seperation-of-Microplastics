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

Colors=['red','blue','violet','green','black','yellow']
labels=['PP','PET','PA','HDPE','PS','PVC'] 
Exp='Brett'
UV_folderpath='C:/Users/ritasha/Desktop/Srumika/PHD/gonnade/Brett UV'


# Colors=['red','blue','violet','black','green','yellow']
# labels=['PP','PET','PA','PS','HDPE','PVC'] 
# Exp='BAM'
# UV_folderpath='C:/Users/ritasha/Desktop/Srumika/PHD/gonnade/BAM UV'


filt=['380','400','420','440','460','500']

Allsets=[[[]for _ in range(6)] for _ in range(6)]
Allsetsfiles=[[[]for _ in range(6)] for _ in range(6)]
for i in range(1,7): #sets
    for j in range(len(filt)): # filters
        filters=glob.glob(UV_folderpath+'/RUV_set_'+str(i)+'_F'+filt[j]+'_*')
        for k in range(len(filters)):
            imgdata=cv2.imread(filters[k])
            imgdata=imgdata
            Allsets[j][i-1].append(imgdata) 
        #Allsetsfiles[i-1][j].append(filters) 
#Allsets[x] x indicates sets 1 to 4, Allsets[x][y] y indicates 5 filters, Allsets[x][y][z] indicates 5 measurement replicates

     
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
    l=0
    value=10
    # if x==1:
    #     l=4
    image=Allsets[l][x][0]
    Cont = [] 
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _,thresh = cv2.threshold(gray,value, 255, cv2.THRESH_BINARY )
    thresh = cv2.erode(thresh, np.ones((5,5)))
    _,cnts, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_NONE)
    (cnts, boundingBoxes) = sort_contours(cnts, method="right-to-left")
        
    for (j, c) in enumerate(cnts):
        if cv2.contourArea(c) > 2000:
            Cont.append(c)
            #uncomment to check contouring
            # mask = np.zeros_like(gray)
            # cv2.drawContours(mask,[c],-1, 255, -1)
            # res = cv2.bitwise_and(image,image,mask=mask)
            # res = cv2.resize(res, (960, 540))
            # cv2.imshow('res', res)
            # cv2.waitKey(0)
    return Cont


Samples=[[[]for _ in range(6)] for _ in range(6)] #all filters

for l in range(len(Allsets)):# filters
    for i in range(len(Allsets[l])): #### sets
        for j in range(len(Allsets[l][i])):  #### repetition
            Z = Allsets[l][i][j]
            Cont=subsampling(i) #making contours based on 370 nm filter
            Cont_new=[]
            for r in range(len(Cont)):
                if len(Cont[r])>1000:
                    new=np.array_split(Cont[r], (len(Cont[r])//1000)+2)
                    for n in range(len(new)):
                        Cont_new.append(new[n])
                else:
                    Cont_new.append(Cont[r])
       

            for k in range(0, len(Cont_new)): # no.of samples

                x,y,w,h = cv2.boundingRect(Cont_new[k])
                ROI = Z[y:y+h, x:x+w]
                chanels = [blue, green, red] = ROI[0:1216, 0:1936,0], ROI[0:1216,0:1936,1], ROI[0:1216, 0:1936,2]
                colarr=[blue, green, red] = blue.flatten(), green.flatten(), red.flatten()
        
                Zscore=[Zscore1,Zscore2,Zscore3]=stats.zscore(blue),stats.zscore(green),stats.zscore(red)
               
                channels=[]
                for m in range(3): #to take and average of 3 colors
                    a = np.argwhere(Zscore[m]>(np.min(Zscore[m])+0.5))
                    b=np.argwhere(Zscore[m]<(np.quantile(Zscore[m],0.98)))
                        
                    c= np.intersect1d(a,b)
                    if np.size(c)==0:
                          new_blue=colarr[m]
                    else:
                        new_blue=colarr[m][c] 
                    chan=np.mean(new_blue)
                    channels.append(chan)
                p=0
                colorcombo = channels[p]+channels[p+1]
                
                Samples[l][i].append(colorcombo) # i indicates filters
                #SamplesSTD[i][k].append(STD)

folderpath='C:/Users/ritasha/Desktop/Srumika/PHD/gonnade/Results'

fig, ax = plt.subplots()
fig.suptitle(Exp)
plt.subplots_adjust(hspace=0.2,wspace=0.15)


axx=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2]]


for i in range(6): #sample type
    if i==3:
                i=4
    elif i==4:
                i=3
    else:
                i=i        
    for j in range(len(Samples[0][i])):
                P1=Samples[0][i][j]/Samples[5][i][j]
                P2=Samples[3][i][j]/Samples[4][i][j]
                ax.scatter(P1,P2,marker='s',c=Colors[i],alpha=0.5)  
    ax.scatter(P1,P2,marker='s',c=Colors[i],alpha=0.5,label=labels[i]) 
    ax.set_xlabel('P1=380/500')
    ax.set_ylabel('P2=420/440')
    ax.set_xlim(0,4)
    ax.set_ylim(0,2)

plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.20),ncol=4)   

plt.savefig(folderpath+'/'+Exp+'_UVparms.png',dpi=1000, transparent=False, papertype=None,bbox_inches='tight')



fig, axs = plt.subplots(2,3)
fig.suptitle(Exp)
plt.subplots_adjust(hspace=0.2,wspace=0.15)

axx=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2]]
for k in range(6): #filters  
    for i in range(6): #sample type
            m=axx[i][0]
            n=axx[i][1]
            l=[5,4,3,2,1,0]
            if i==3:
                i=4
            elif i==4:
                i=3
            else:
                i=i
            axs[m,n].scatter(Samples[k][i][:],[l[k]]*len(Samples[k][i][:]),marker='s',c=Colors[i],alpha=0.5,label=labels[i])    
            axs[m,n].axhline(y=l[k]-0.5, color='black', linestyle='-')
            axs[m,n].set_title(labels[i])
            #axs[m,n].set_ylim(-0.4,1.4)
            axs[m,n].set_yticks([])
            if i<3:
                axs[m,n].set_xticks([])
            axs[m,n].set_xlim([0,500])
#plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.50),ncol=4)   

plt.savefig(folderpath+'/'+Exp+'_UV.png',dpi=1000, transparent=False, papertype=None,bbox_inches='tight')

