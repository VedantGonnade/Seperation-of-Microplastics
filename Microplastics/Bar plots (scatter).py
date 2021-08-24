# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 11:45:06 2020

@author: Admin
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2
import glob
from scipy import integrate

F440 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 06.11.2020\Plastics\PPH\Measurements/F440/*')
F460 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 06.11.2020\Plastics\PPH\Measurements/F460/*')
F500 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 06.11.2020\Plastics\PPH\Measurements/F500/*')
F560 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 06.11.2020\Plastics\PPH\Measurements/F560/*')
F610 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 06.11.2020\Plastics\PPH\Measurements/F610/*')
PET_all = [F440, F460, F500, F560, F610]
STD_1, STD_2, STD_3, STD_4, STD_5, STD_6, STD_7, STD_8, STD_9 = [], [], [], [], [], [], [], [], []
STD_filter = [STD_1, STD_2, STD_3, STD_4, STD_5, STD_6, STD_7, STD_8, STD_9]
Mean_STD = []

for i in range(len(PET_all)):
    z = cv2.imread(PET_all[i][0], -1)
    row, col = (np.argmax(z)//z.shape[1],  np.argmax(z)%z.shape[1])
    
    for i in range(1,10):
        row_min = row - i
        row_max = row + i
        col_min = col - i
        col_max = col + i
        Pix=z[row_min:row_max + i, col_min:col_max+ i]
        MeanP=np.mean(Pix)
        StdP=np.std(Pix) 
        
        if (i == 1):
            STD_1.append(StdP)
        elif i == 2:
            STD_2.append(StdP)
        elif i == 3:
            STD_3.append(StdP)
        elif i == 4:
            STD_4.append(StdP)
        elif i == 5:
            STD_5.append(StdP)    
        elif i == 6:
            STD_6.append(StdP)
        elif i == 7:
            STD_7.append(StdP)
        elif i == 8:
            STD_8.append(StdP)     
        else:
            STD_9.append(StdP)
            
for i in range(9):
    Mean_STD.append(np.mean(STD_filter[i]))
Matrix = 0

Mean440, Mean460, Mean500, Mean560 , Mean610 = [], [], [], [], []   
STD440, STD460, STD500, STD560, STD610 = [], [], [], [], []
MeanI = [Mean440, Mean460, Mean500, Mean560 , Mean610]
STD_all = [STD440, STD460, STD500, STD560, STD610]
Final_intensity = []
Final_STD = []

for i in range(len(PET_all)):
    for j in range(5):
        img = cv2.imread(PET_all[i][j], -1)
        row, col = (np.argmax(img)//img.shape[1],  np.argmax(img)%img.shape[1])
        row_min = row - Matrix -1
        row_max = row + Matrix +1
        col_min = col - Matrix -1
        col_max = col + Matrix +1
        Pix=img[row_min:row_max+1, col_min:col_max+1]
        MeanP=np.mean(Pix)       
        StdP=np.std(Pix)
        
        if i == 0:
            Mean440.append(MeanP)
            STD440.append(StdP)
        elif i == 1:
            Mean460.append(MeanP)
            STD460.append(StdP)
        elif i == 2:
            Mean500.append(MeanP)
            STD500.append(StdP)
        elif i == 3:
            Mean560.append(MeanP)
            STD560.append(StdP)
        else:
            Mean610.append(MeanP)
            STD610.append(StdP)
       
for i in range(5):
    Final_intensity.append(np.mean(MeanI[i]))
    Final_STD.append(np.mean(STD_all[i]))
    
Xaxis = [440, 460, 500, 560, 610]
    
fig, ax = plt.subplots(dpi = 250)
graph = ax.bar(Xaxis, Final_intensity,width = 2, yerr=Final_STD, align='center', alpha=1, ecolor='black', capsize=10)
#ax.set_ylabel('Mean intensity of 5 images')
ax.set_xlabel('Different filters (nm)')
ax.set_xticks(Xaxis)
ax.set_title('Intensity of PPH using 5 different filters')
ax.yaxis.grid(True)
ax.text(540,157,"Power- 179 mW",color="black", fontdict={"fontsize": 10,"ha":"left","va":"center"})
#graph = ax.scatter(Xaxis, Final_intensity)
#ax.plot(Xaxis, Final_intensity)
# Save the figure and show
plt.tight_layout()
plt.savefig('Wood intensities.png')
integrate.simps(Final_intensity)
plt.show()

print(integrate.simps(Final_intensity))

