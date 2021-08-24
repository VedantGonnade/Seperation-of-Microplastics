# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 19:46:30 2021

@author: ritasha
"""
import csv
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
from scipy.signal import savgol_filter
C1=[]
C2=[]
with open('F:\Multispectral Imaging\Beam size calculation\horizontal.csv', 'r') as file:
    reader = csv.reader(file)
    
    listR=list(reader)
    
    for i in range(1,len(listR)):
        C1.append(int(float(listR[i][0])))
        C2.append(int(float(listR[i][1])))
        
    #print(C1)
    #print(C2)


x=np.array(C1)
y=np.array(C2)
# = savgol_filter(x, 151, 2)
y=savgol_filter(y, 101, 2)
# weighted arithmetic mean (corrected - check the section below)
mean = sum(x * y) / sum(y)
sigma = np.sqrt(np.abs(sum(y * (x - mean)**2) / sum(y)))
#sigma = np.sqrt(sum(y * (x - mean)**2) / sum(y))


def Gauss(x, a, x0, sigma):
    return a * np.exp(-(x - x0)**2 / (2 * sigma**2))
def lin_interp(x, y, i, half):
    return x[i] + (x[i+1] - x[i]) * ((half - y[i]) / (y[i+1] - y[i]))

def half_max_x(x, y):
    half = max(y)/2.0
    signs = np.sign(np.add(y, -half))
    zero_crossings = (signs[0:-2] != signs[1:-1])
    zero_crossings_i = np.where(zero_crossings)[0]
    return [lin_interp(x, y, zero_crossings_i[0], half),
            lin_interp(x, y, zero_crossings_i[1], half)]

# find the two crossing points
hmx = half_max_x(x,y)

# print the answer
fwhm = hmx[1] - hmx[0]
print("FWHM:{:.3f}".format(fwhm))
half = max(y)/2.0
plt.plot(x,y)
plt.plot(hmx, [half, half])
plt.show()


plt.figure()

plt.plot(x,y,'b+:', label='data')    
popt,pcov = curve_fit(Gauss, x,y, p0=[max(y), mean, sigma])
plt.plot(x, Gauss(x, *popt), 'r-', label='fit')


      
plt.show()


