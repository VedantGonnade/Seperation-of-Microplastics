# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 15:19:41 2020

@author: Admin
"""
import numpy as np
import matplotlib.pyplot as plt
import cv2
import glob
from scipy import integrate

PPH_F440 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 24.11.2020\Plastics\PPH\Measurements\F440/*')
PPH_F460 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 24.11.2020\Plastics\PPH\Measurements/F460/*')
PPH_F500 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 24.11.2020\Plastics\PPH\Measurements/F500/*')
PPH_F560 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 24.11.2020\Plastics\PPH\Measurements/F560/*')
PPH_F610 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 24.11.2020\Plastics\PPH\Measurements/F610/*')
PPH_all = [PPH_F440, PPH_F460, PPH_F500, PPH_F560, PPH_F610]

PE500_F440 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 24.11.2020\Plastics\PE 500\Measurements/F440/*')
PE500_F460 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 24.11.2020\Plastics\PE 500\Measurements/F460/*')
PE500_F500 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 24.11.2020\Plastics\PE 500\Measurements/F500/*')
PE500_F560 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 24.11.2020\Plastics\PE 500\Measurements/F560/*')
PE500_F610 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 24.11.2020\Plastics\PE 500\Measurements/F610/*')
PE500_all = [PE500_F440, PE500_F460, PE500_F500, PE500_F560, PE500_F610]

PE1000_F440 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 24.11.2020\Plastics\PE 1000\Measurements/F440/*')
PE1000_F460 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 24.11.2020\Plastics\PE 1000\Measurements/F460/*')
PE1000_F500 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 24.11.2020\Plastics\PE 1000\Measurements/F500/*')
PE1000_F560 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 24.11.2020\Plastics\PE 1000\Measurements/F560/*')
PE1000_F610 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 24.11.2020\Plastics\PE 1000\Measurements/F610/*')
PE1000_all = [PE1000_F440, PE1000_F460, PE1000_F500, PE1000_F560, PE1000_F610]

# PS_F440 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 24.11.2020\Plastics\PS\Measurements/F440/*')
# PS_F460 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 24.11.2020\Plastics\PS\Measurements/F460/*')
# PS_F500 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 24.11.2020\Plastics\PS\Measurements/F500/*')
# PS_F560 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 24.11.2020\Plastics\PS\Measurements/F560/*')
# PS_F610 = glob.glob('F:\Multispectral Imaging\Readings\Readings on 24.11.2020\Plastics\PS\Measurements/F610/*')
# PS_all = [PS_F440, PS_F460, PS_F500, PS_F560, PS_F610]

Samples_170mW = [PPH_all, PE500_all, PE1000_all]
Matrix = 0

MeanPPH = []   
PPH_individual = [PPH1, PPH2, PPH3, PPH4, PPH5] = [], [], [], [], []
PPHdeviations = []
PPH_individual_deviations = [PPH_dev440, PPH_dev460, PPH_dev500, PPH_dev560, PPH_dev610 ] = [], [], [], [], []
PPH_final_deviation = []


MeanPE500 = [] 
PE500_individual = [PE5001, PE5002, PE5003, PE5004, PE5005] = [], [], [], [], []
PE500deviations = []
PE500_individual_deviations = [PE500_dev440, PE500_dev460, PE500_dev500, PE500_dev560, PE500_dev610 ] = [], [], [], [], []
PE500_final_deviation = []


MeanPE1000 = []  
PE1000_individual = [PE10001, PE10002, PE10003, PE10004, PE10005] = [], [], [], [], []
PE1000deviations = []
PE1000_individual_deviations = [PE1000_dev440, PE1000_dev460, PE1000_dev500, PE1000_dev560, PE1000_dev610 ] = [], [], [], [], []
PE1000_final_deviation = []

# MeanPS = []   
# PS_individual = [PS1, PS2, PS3, PS4, PS5] = [], [], [], [], []
# PSdeviations = []
# PS_individual_deviations = [PS_dev440, PS_dev460, PS_dev500, PS_dev560, PS_dev610 ] = [], [], [], [], []
# PS_final_deviation = []


'''POWER CONVERSION FUCTIONS'''
for i in range(len(PPH_all)):
    for k in range(5):
        img = cv2.imread(PPH_all[i][k], -1)
        row, col = (np.argmax(img)//img.shape[1],  np.argmax(img)%img.shape[1])
        row_min = row - Matrix -1
        row_max = row + Matrix +1
        col_min = col - Matrix -1
        col_max = col + Matrix +1
        Pix=img[row_min:row_max+1, col_min:col_max+1]
        MeanP=np.mean(Pix) * ( 5.0/ 181)
        
        if i == 0:
            if k == 0:
                PPH_all[i][k] = MeanP
            if k == 1:
                PPH_all[i][k] = MeanP
            if k == 2:
                PPH_all[i][k] = MeanP
            if k == 3:
                PPH_all[i][k] = MeanP
            if k == 4:
                PPH_all[i][k] = MeanP
                
        elif i == 1:
            if k == 0:
                PPH_all[i][k] = MeanP
            if k == 1:
                PPH_all[i][k] = MeanP
            if k == 2:
                PPH_all[i][k] = MeanP
            if k == 3:
                PPH_all[i][k] = MeanP
            if k == 4:
                PPH_all[i][k] = MeanP
            
        elif i == 2:
            if k == 0:
                PPH_all[i][k] = MeanP
            if k == 1:
                PPH_all[i][k] = MeanP
            if k == 2:
                PPH_all[i][k] = MeanP
            if k == 3:
                PPH_all[i][k] = MeanP
            if k == 4:
                PPH_all[i][k] = MeanP
            
        elif i == 3:
            if k == 0:
                PPH_all[i][k] = MeanP
            if k == 1:
                PPH_all[i][k] = MeanP
            if k == 2:
                PPH_all[i][k] = MeanP
            if k == 3:
                PPH_all[i][k] = MeanP
            if k == 4:
                PPH_all[i][k] = MeanP
            
        elif i == 4:
            if k == 0:
                PPH_all[i][k] = MeanP
            if k == 1:
                PPH_all[i][k] = MeanP
            if k == 2:
                PPH_all[i][k] = MeanP
            if k == 3:
                PPH_all[i][k] = MeanP
            if k == 4:
                PPH_all[i][k] = MeanP
        

for i in range(len(PE500_all)):
    for k in range(5):
        img = cv2.imread(PE500_all[i][k], -1)
        row, col = (np.argmax(img)//img.shape[1],  np.argmax(img)%img.shape[1])
        row_min = row - Matrix -1
        row_max = row + Matrix +1
        col_min = col - Matrix -1
        col_max = col + Matrix +1
        Pix=img[row_min:row_max+1, col_min:col_max+1]
        MeanP=np.mean(Pix) * (5.0 / 181)
        
        if i == 0:
            if k == 0:
                PE500_all[i][k] = MeanP
            if k == 1:
                PE500_all[i][k] = MeanP
            if k == 2:
                PE500_all[i][k] = MeanP
            if k == 3:
                PE500_all[i][k] = MeanP
            if k == 4:
                PE500_all[i][k] = MeanP
                
        elif i == 1:
            if k == 0:
                PE500_all[i][k] = MeanP
            if k == 1:
                PE500_all[i][k] = MeanP
            if k == 2:
                PE500_all[i][k] = MeanP
            if k == 3:
                PE500_all[i][k] = MeanP
            if k == 4:
                PE500_all[i][k] = MeanP
            
        elif i == 2:
            if k == 0:
                PE500_all[i][k] = MeanP
            if k == 1:
                PE500_all[i][k] = MeanP
            if k == 2:
                PE500_all[i][k] = MeanP
            if k == 3:
                PE500_all[i][k] = MeanP
            if k == 4:
                PE500_all[i][k] = MeanP
            
        elif i == 3:
            if k == 0:
                PE500_all[i][k] = MeanP
            if k == 1:
                PE500_all[i][k] = MeanP
            if k == 2:
                PE500_all[i][k] = MeanP
            if k == 3:
                PE500_all[i][k] = MeanP
            if k == 4:
                PE500_all[i][k] = MeanP
            
        elif i == 4:
            if k == 0:
                PE500_all[i][k] = MeanP
            if k == 1:
                PE500_all[i][k] = MeanP
            if k == 2:
                PE500_all[i][k] = MeanP
            if k == 3:
                PE500_all[i][k] = MeanP
            if k == 4:
                PE500_all[i][k] = MeanP
       
for i in range(len(PE1000_all)):
    for k in range(5):
        img = cv2.imread(PE1000_all[i][k], -1)
        row, col = (np.argmax(img)//img.shape[1],  np.argmax(img)%img.shape[1])
        row_min = row - Matrix -1
        row_max = row + Matrix +1
        col_min = col - Matrix -1
        col_max = col + Matrix +1
        Pix=img[row_min:row_max+1, col_min:col_max+1]
        MeanP=np.mean(Pix) * (5.0/181)
        
        if i == 0:
            if k == 0:
                PE1000_all[i][k] = MeanP
            if k == 1:
                PE1000_all[i][k] = MeanP
            if k == 2:
                PE1000_all[i][k] = MeanP
            if k == 3:
                PE1000_all[i][k] = MeanP
            if k == 4:
                PE1000_all[i][k] = MeanP
                
        elif i == 1:
            if k == 0:
                PE1000_all[i][k] = MeanP
            if k == 1:
                PE1000_all[i][k] = MeanP
            if k == 2:
                PE1000_all[i][k] = MeanP
            if k == 3:
                PE1000_all[i][k] = MeanP
            if k == 4:
                PE1000_all[i][k] = MeanP
            
        elif i == 2:
            if k == 0:
                PE1000_all[i][k] = MeanP
            if k == 1:
                PE1000_all[i][k] = MeanP
            if k == 2:
                PE1000_all[i][k] = MeanP
            if k == 3:
                PE1000_all[i][k] = MeanP
            if k == 4:
                PE1000_all[i][k] = MeanP
            
        elif i == 3:
            if k == 0:
                PE1000_all[i][k] = MeanP
            if k == 1:
                PE1000_all[i][k] = MeanP
            if k == 2:
                PE1000_all[i][k] = MeanP
            if k == 3:
                PE1000_all[i][k] = MeanP
            if k == 4:
                PE1000_all[i][k] = MeanP
            
        elif i == 4:
            if k == 0:
                PE1000_all[i][k] = MeanP
            if k == 1:
                PE1000_all[i][k] = MeanP
            if k == 2:
                PE1000_all[i][k] = MeanP
            if k == 3:
                PE1000_all[i][k] = MeanP
            if k == 4:
                PE1000_all[i][k] = MeanP
                
# for i in range(len(PS_all)):
#     for k in range(5):
#         img = cv2.imread(PS_all[i][k], -1)
#         row, col = (np.argmax(img)//img.shape[1],  np.argmax(img)%img.shape[1])
#         row_min = row - Matrix -1
#         row_max = row + Matrix +1
#         col_min = col - Matrix -1
#         col_max = col + Matrix +1
#         Pix=img[row_min:row_max+1, col_min:col_max+1]
#         MeanP=np.mean(Pix) * (5.0 / 18.86)
        
#         if i == 0:
#             if k == 0:
#                 PS_all[i][k] = MeanP
#             if k == 1:
#                 PS_all[i][k] = MeanP
#             if k == 2:
#                 PS_all[i][k] = MeanP
#             if k == 3:
#                 PS_all[i][k] = MeanP
#             if k == 4:
#                 PS_all[i][k] = MeanP
                
#         elif i == 1:
#             if k == 0:
#                 PS_all[i][k] = MeanP
#             if k == 1:
#                 PS_all[i][k] = MeanP
#             if k == 2:
#                 PS_all[i][k] = MeanP
#             if k == 3:
#                 PS_all[i][k] = MeanP
#             if k == 4:
#                 PS_all[i][k] = MeanP
            
#         elif i == 2:
#             if k == 0:
#                 PS_all[i][k] = MeanP
#             if k == 1:
#                 PS_all[i][k] = MeanP
#             if k == 2:
#                 PS_all[i][k] = MeanP
#             if k == 3:
#                 PS_all[i][k] = MeanP
#             if k == 4:
#                 PS_all[i][k] = MeanP
            
#         elif i == 3:
#             if k == 0:
#                 PS_all[i][k] = MeanP
#             if k == 1:
#                 PS_all[i][k] = MeanP
#             if k == 2:
#                 PS_all[i][k] = MeanP
#             if k == 3:
#                 PS_all[i][k] = MeanP
#             if k == 4:
#                 PS_all[i][k] = MeanP
            
#         elif i == 4:
#             if k == 0:
#                 PS_all[i][k] = MeanP
#             if k == 1:
#                 PS_all[i][k] = MeanP
#             if k == 2:
#                 PS_all[i][k] = MeanP
#             if k == 3:
#                 PS_all[i][k] = MeanP
#             if k == 4:
#                 PS_all[i][k] = MeanP
''' POWER CONVERSION FUNCTIONS ENDS'''
        

for i in range(len(Samples_170mW)):
    for j in range(5):                         
            if i == 0:
                if j == 0:
                    MeanPPH.append(np.mean(Samples_170mW[i][j]))  
                    for k in range(5):                 
                        if k == 0:
                            PPH1.append(Samples_170mW[i][j][k])
                        if k == 1:
                            PPH2.append(Samples_170mW[i][j][k])
                        if k == 2:
                            PPH3.append(Samples_170mW[i][j][k])
                        if k == 3:
                            PPH4.append(Samples_170mW[i][j][k])
                        if k == 4:
                            PPH5.append(Samples_170mW[i][j][k])
                            
                if j == 1:
                    MeanPPH.append(np.mean(Samples_170mW[i][j]))
                    for k in range(5): 
                        if k == 0:
                            PPH1.append(Samples_170mW[i][j][k])
                        if k == 1:
                            PPH2.append(Samples_170mW[i][j][k])
                        if k == 2:
                            PPH3.append(Samples_170mW[i][j][k])
                        if k == 3:
                            PPH4.append(Samples_170mW[i][j][k])
                        if k == 4:
                            PPH5.append(Samples_170mW[i][j][k])
                        
                if j == 2:
                    MeanPPH.append(np.mean(Samples_170mW[i][j]))
                    for k in range(5): 
                        if k == 0:
                            PPH1.append(Samples_170mW[i][j][k])
                        if k == 1:
                            PPH2.append(Samples_170mW[i][j][k])
                        if k == 2:
                            PPH3.append(Samples_170mW[i][j][k])
                        if k == 3:
                            PPH4.append(Samples_170mW[i][j][k])
                        if k == 4:
                            PPH5.append(Samples_170mW[i][j][k])
                        
                if j == 3:
                    MeanPPH.append(np.mean(Samples_170mW[i][j]))
                    for k in range(5): 
                        if k == 0:
                            PPH1.append(Samples_170mW[i][j][k])
                        if k == 1:
                            PPH2.append(Samples_170mW[i][j][k])
                        if k == 2:
                            PPH3.append(Samples_170mW[i][j][k])
                        if k == 3:
                            PPH4.append(Samples_170mW[i][j][k])
                        if k == 4:
                            PPH5.append(Samples_170mW[i][j][k])
                        
                if j == 4:
                    MeanPPH.append(np.mean(Samples_170mW[i][j]))
                    for k in range(5): 
                        if k == 0:
                            PPH1.append(Samples_170mW[i][j][k])
                        if k == 1:
                            PPH2.append(Samples_170mW[i][j][k])
                        if k == 2:
                            PPH3.append(Samples_170mW[i][j][k])
                        if k == 3:
                            PPH4.append(Samples_170mW[i][j][k])
                        if k == 4:
                            PPH5.append(Samples_170mW[i][j][k])
                       
            elif i == 1:
                if j == 0:
                    MeanPE500.append(np.mean(Samples_170mW[i][j]))
                    for k in range(5): 
                        if k == 0:
                            PE5001.append(Samples_170mW[i][j][k])
                        if k == 1:
                            PE5002.append(Samples_170mW[i][j][k])
                        if k == 2:
                            PE5003.append(Samples_170mW[i][j][k])
                        if k == 3:
                            PE5004.append(Samples_170mW[i][j][k])
                        if k == 4:
                            PE5005.append(Samples_170mW[i][j][k])
    
                if j == 1:
                    MeanPE500.append(np.mean(Samples_170mW[i][j]))
                    for k in range(5):
                        if k == 0:
                            PE5001.append(Samples_170mW[i][j][k])
                        if k == 1:
                            PE5002.append(Samples_170mW[i][j][k])
                        if k == 2:
                            PE5003.append(Samples_170mW[i][j][k])
                        if k == 3:
                            PE5004.append(Samples_170mW[i][j][k])
                        if k == 4:
                            PE5005.append(Samples_170mW[i][j][k])
                    
                if j == 2:
                    MeanPE500.append(np.mean(Samples_170mW[i][j]))
                    for k in range(5):
                        if k == 0:
                            PE5001.append(Samples_170mW[i][j][k])
                        if k == 1:
                            PE5002.append(Samples_170mW[i][j][k])
                        if k == 2:
                            PE5003.append(Samples_170mW[i][j][k])
                        if k == 3:
                            PE5004.append(Samples_170mW[i][j][k])
                        if k == 4:
                            PE5005.append(Samples_170mW[i][j][k])
                    
                if j == 3:
                    MeanPE500.append(np.mean(Samples_170mW[i][j]))
                    for k in range(5):
                        if k == 0:
                            PE5001.append(Samples_170mW[i][j][k])
                        if k == 1:
                            PE5002.append(Samples_170mW[i][j][k])
                        if k == 2:
                            PE5003.append(Samples_170mW[i][j][k])
                        if k == 3:
                            PE5004.append(Samples_170mW[i][j][k])
                        if k == 4:
                            PE5005.append(Samples_170mW[i][j][k])
    
                if j == 4:
                    MeanPE500.append(np.mean(Samples_170mW[i][j]))
                    for k in range(5):
                        if k == 0:
                            PE5001.append(Samples_170mW[i][j][k])
                        if k == 1:
                            PE5002.append(Samples_170mW[i][j][k])
                        if k == 2:
                            PE5003.append(Samples_170mW[i][j][k])
                        if k == 3:
                            PE5004.append(Samples_170mW[i][j][k])
                        if k == 4:
                            PE5005.append(Samples_170mW[i][j][k])
                 
            elif i == 2:
                if j == 0:
                    MeanPE1000.append(np.mean(Samples_170mW[i][j]))
                    for k in range(5):
                        if k == 0:
                            PE10001.append(Samples_170mW[i][j][k])
                        if k == 1:
                            PE10002.append(Samples_170mW[i][j][k])
                        if k == 2:
                            PE10003.append(Samples_170mW[i][j][k])
                        if k == 3:
                            PE10004.append(Samples_170mW[i][j][k])
                        if k == 4:
                            PE10005.append(Samples_170mW[i][j][k])
                            
                if j == 1:
                    MeanPE1000.append(np.mean(Samples_170mW[i][j]))
                    for k in range(5):
                        if k == 0:
                            PE10001.append(Samples_170mW[i][j][k])
                        if k == 1:
                            PE10002.append(Samples_170mW[i][j][k])
                        if k == 2:
                            PE10003.append(Samples_170mW[i][j][k])
                        if k == 3:
                            PE10004.append(Samples_170mW[i][j][k])
                        if k == 4:
                            PE10005.append(Samples_170mW[i][j][k])
                            
                if j == 2:
                    MeanPE1000.append(np.mean(Samples_170mW[i][j]))
                    for k in range(5):
                        if k == 0:
                            PE10001.append(Samples_170mW[i][j][k])
                        if k == 1:
                            PE10002.append(Samples_170mW[i][j][k])
                        if k == 2:
                            PE10003.append(Samples_170mW[i][j][k])
                        if k == 3:
                            PE10004.append(Samples_170mW[i][j][k])
                        if k == 4:
                            PE10005.append(Samples_170mW[i][j][k])
                            
                if j == 3:
                    MeanPE1000.append(np.mean(Samples_170mW[i][j]))
                    for k in range(5):
                        if k == 0:
                            PE10001.append(Samples_170mW[i][j][k])
                        if k == 1:
                            PE10002.append(Samples_170mW[i][j][k])
                        if k == 2:
                            PE10003.append(Samples_170mW[i][j][k])
                        if k == 3:
                            PE10004.append(Samples_170mW[i][j][k])
                        if k == 4:
                            PE10005.append(Samples_170mW[i][j][k])
                            
                if j == 4:
                    MeanPE1000.append(np.mean(Samples_170mW[i][j]))
                    for k in range(5):
                        if k == 0:
                            PE10001.append(Samples_170mW[i][j][k])
                        if k == 1:
                            PE10002.append(Samples_170mW[i][j][k])
                        if k == 2:
                            PE10003.append(Samples_170mW[i][j][k])
                        if k == 3:
                            PE10004.append(Samples_170mW[i][j][k])
                        if k == 4:
                            PE10005.append(Samples_170mW[i][j][k])
            # elif i == 3:
            #     if j == 0:
            #         MeanPS.append(np.mean(Samples_170mW[i][j]))
            #         for k in range(5):
            #             if k == 0:
            #                 PS1.append(Samples_170mW[i][j][k])
            #             if k == 1:
            #                 PS2.append(Samples_170mW[i][j][k])
            #             if k == 2:
            #                 PS3.append(Samples_170mW[i][j][k])
            #             if k == 3:
            #                 PS4.append(Samples_170mW[i][j][k])
            #             if k == 4:
            #                 PS5.append(Samples_170mW[i][j][k])
                            
            #     if j == 1:
            #         MeanPS.append(np.mean(Samples_170mW[i][j]))
            #         for k in range(5):
            #             if k == 0:
            #                 PS1.append(Samples_170mW[i][j][k])
            #             if k == 1:
            #                 PS2.append(Samples_170mW[i][j][k])
            #             if k == 2:
            #                 PS3.append(Samples_170mW[i][j][k])
            #             if k == 3:
            #                 PS4.append(Samples_170mW[i][j][k])
            #             if k == 4:
            #                 PS5.append(Samples_170mW[i][j][k])
                            
            #     if j == 2:
            #         MeanPS.append(np.mean(Samples_170mW[i][j]))
            #         for k in range(5):
            #             if k == 0:
            #                 PS1.append(Samples_170mW[i][j][k])
            #             if k == 1:
            #                 PS2.append(Samples_170mW[i][j][k])
            #             if k == 2:
            #                 PS3.append(Samples_170mW[i][j][k])
            #             if k == 3:
            #                 PS4.append(Samples_170mW[i][j][k])
            #             if k == 4:
            #                 PS5.append(Samples_170mW[i][j][k])
                            
            #     if j == 3:
            #         MeanPS.append(np.mean(Samples_170mW[i][j]))
            #         for k in range(5):
            #             if k == 0:
            #                 PS1.append(Samples_170mW[i][j][k])
            #             if k == 1:
            #                 PS2.append(Samples_170mW[i][j][k])
            #             if k == 2:
            #                 PS3.append(Samples_170mW[i][j][k])
            #             if k == 3:
            #                 PS4.append(Samples_170mW[i][j][k])
            #             if k == 4:
            #                 PS5.append(Samples_170mW[i][j][k])
                            
            #     if j == 4:
            #         MeanPS.append(np.mean(Samples_170mW[i][j]))
            #         for k in range(5):
            #             if k == 0:
            #                 PS1.append(Samples_170mW[i][j][k])
            #             if k == 1:
            #                 PS2.append(Samples_170mW[i][j][k])
            #             if k == 2:
            #                 PS3.append(Samples_170mW[i][j][k])
            #             if k == 3:
            #                 PS4.append(Samples_170mW[i][j][k])
            #             if k == 4:
            #                 PS5.append(Samples_170mW[i][j][k])
           
                                   


'''deviation with normalizing'''

PPH_integrate_values = []
for i in PPH_individual:
    values = integrate.simps(i)
    PPH_integrate_values.append(values)

PE500_integrate_values = []
for i in PE500_individual:
    values = integrate.simps(i)
    PE500_integrate_values.append(values)    
    
PE1000_integrate_values = []
for i in PE1000_individual:
    values = integrate.simps(i)
    PE1000_integrate_values.append(values) 

# # PS_integrate_values = []
# # for i in PS_individual:
# #     values = integrate.simps(i)
# #     PS_integrate_values.append(values)
    


for i in range(len(PPH_individual)):
    if i == 0:
        value = PPH_individual[i]/PPH_integrate_values[0]
        PPHdeviations.append(value)
    if i == 1:
        value = PPH_individual[i]/PPH_integrate_values[1]
        PPHdeviations.append(value)
    if i == 2:
        value = PPH_individual[i]/PPH_integrate_values[2]
        PPHdeviations.append(value)
    if i == 3:
        value = PPH_individual[i]/PPH_integrate_values[3]
        PPHdeviations.append(value)
    if i == 4:
        value = PPH_individual[i]/PPH_integrate_values[4]
        PPHdeviations.append(value)

for i in range(len(PE500_individual)):
    if i == 0:
        value = PE500_individual[i]/PE500_integrate_values[0]
        PE500deviations.append(value)
    if i == 1:
        value = PE500_individual[i]/PE500_integrate_values[1]
        PE500deviations.append(value)
    if i == 2:
        value = PE500_individual[i]/PE500_integrate_values[2]
        PE500deviations.append(value)
    if i == 3:
        value = PE500_individual[i]/PE500_integrate_values[3]
        PE500deviations.append(value)
    if i == 4:
        value = PE500_individual[i]/PE500_integrate_values[4]
        PE500deviations.append(value)
        
for i in range(len(PE1000_individual)):
    if i == 0:
        value = PE1000_individual[i]/PE1000_integrate_values[0]
        PE1000deviations.append(value)
    if i == 1:
        value = PE1000_individual[i]/PE1000_integrate_values[1]
        PE1000deviations.append(value)
    if i == 2:
        value = PE1000_individual[i]/PE1000_integrate_values[2]
        PE1000deviations.append(value)
    if i == 3:
        value = PE1000_individual[i]/PE1000_integrate_values[3]
        PE1000deviations.append(value)
    if i == 4:
        value = PE1000_individual[i]/PE1000_integrate_values[4]
        PE1000deviations.append(value)
    
# # for i in range(len(PS_individual)):
# #     if i == 0:
# #         value = PS_individual[i]/PS_integrate_values[0]
# #         PSdeviations.append(value)
# #     if i == 1:
# #         value = PS_individual[i]/PS_integrate_values[1]
# #         PSdeviations.append(value)
# #     if i == 2:
# #         value = PS_individual[i]/PS_integrate_values[2]
# #         PSdeviations.append(value)
# #     if i == 3:
# #         value = PS_individual[i]/PS_integrate_values[3]
# #         PSdeviations.append(value)
# #     if i == 4:
# #         value = PS_individual[i]/PS_integrate_values[4]
# #         PSdeviations.append(value)
        
  
for i in range(len(PPHdeviations)):
    for j in range(5):
        if j == 0:
            PPH_dev440.append(PPHdeviations[i][j])
        if j == 1:
            PPH_dev460.append(PPHdeviations[i][j])
        if j == 2:
            PPH_dev500.append(PPHdeviations[i][j])
        if j == 3:
            PPH_dev560.append(PPHdeviations[i][j])
        if j == 4:
            PPH_dev610.append(PPHdeviations[i][j])

for i in range(len(PE500deviations)):
    for j in range(5):
        if j == 0:
            PE500_dev440.append(PE500deviations[i][j])
        if j == 1:
            PE500_dev460.append(PE500deviations[i][j])
        if j == 2:
            PE500_dev500.append(PE500deviations[i][j])
        if j == 3:
            PE500_dev560.append(PE500deviations[i][j])
        if j == 4:
            PE500_dev610.append(PE500deviations[i][j])
            
for i in range(len(PE1000deviations)):
    for j in range(5):
        if j == 0:
            PE1000_dev440.append(PE1000deviations[i][j])
        if j == 1:
            PE1000_dev460.append(PE1000deviations[i][j])
        if j == 2:
            PE1000_dev500.append(PE1000deviations[i][j])
        if j == 3:
            PE1000_dev560.append(PE1000deviations[i][j])
        if j == 4:
            PE1000_dev610.append(PE1000deviations[i][j])
             
# # for i in range(len(PSdeviations)):
# #     for j in range(5):
# #         if j == 0:
# #             PS_dev440.append(PSdeviations[i][j])
# #         if j == 1:
# #             PS_dev460.append(PSdeviations[i][j])
# #         if j == 2:
# #             PS_dev500.append(PSdeviations[i][j])
# #         if j == 3:
# #             PS_dev560.append(PSdeviations[i][j])
# #         if j == 4:
# #             PS_dev610.append(PSdeviations[i][j])          


for i in PPH_individual_deviations:
    value = np.std(i)
    PPH_final_deviation.append(value)
    
for i in PE500_individual_deviations:
    value = np.std(i)
    PE500_final_deviation.append(value)
    
for i in PE1000_individual_deviations:
    value = np.std(i)
    PE1000_final_deviation.append(value)
    
# # for i in PS_individual_deviations:
# #     value = np.std(i)
# #     PS_final_deviation.append(value)     
'''ends here'''            
            
'''deviation without normalizing starts here'''

# for i in range(len(PPH_individual)):
#     for j in range(5):
#         if j == 0:
#             PPH_dev440.append(PPH_individual[i][j])
#         if j == 1:
#             PPH_dev460.append(PPH_individual[i][j])
#         if j == 2:
#             PPH_dev500.append(PPH_individual[i][j])
#         if j == 3:
#             PPH_dev560.append(PPH_individual[i][j])
#         if j == 4:
#             PPH_dev610.append(PPH_individual[i][j])

# for i in range(len(PE500_individual)):
#     for j in range(5):
#         if j == 0:
#             PE500_dev440.append(PE500_individual[i][j])
#         if j == 1:
#             PE500_dev460.append(PE500_individual[i][j])
#         if j == 2:
#             PE500_dev500.append(PE500_individual[i][j])
#         if j == 3:
#             PE500_dev560.append(PE500_individual[i][j])
#         if j == 4:
#             PE500_dev610.append(PE500_individual[i][j])
            
# for i in range(len(PE1000_individual)):
#     for j in range(5):
#         if j == 0:
#             PE1000_dev440.append(PE1000_individual[i][j])
#         if j == 1:
#             PE1000_dev460.append(PE1000_individual[i][j])
#         if j == 2:
#             PE1000_dev500.append(PE1000_individual[i][j])
#         if j == 3:
#             PE1000_dev560.append(PE1000_individual[i][j])
#         if j == 4:
#             PE1000_dev610.append(PE1000_individual[i][j])
             
# for i in range(len(PS_individual)):
#     for j in range(5):
#         if j == 0:
#             PS_dev440.append(PS_individual[i][j])
#         if j == 1:
#             PS_dev460.append(PS_individual[i][j])
#         if j == 2:
#             PS_dev500.append(PS_individual[i][j])
#         if j == 3:
#             PS_dev560.append(PS_individual[i][j])
#         if j == 4:
#             PS_dev610.append(PS_individual[i][j])            
                        
# for i in PPH_individual_deviations:
#     value = np.std(i)
#     PPH_final_deviation.append(value)
    
# for i in PE500_individual_deviations:
#     value = np.std(i)
#     PE500_final_deviation.append(value)
    
# for i in PE1000_individual_deviations:
#     value = np.std(i)
#     PE1000_final_deviation.append(value)
    
# for i in PS_individual_deviations:
#     value = np.std(i)
#     PS_final_deviation.append(value)              


''''without normalizing ende here'''          
          
    
Xaxis = [440, 460, 500, 560, 610]



'''normalizing'''
IntegratePPH = []
#arrayPPH = np.array(PPH_Final_intensity)
IntPPH = integrate.simps(MeanPPH)
for i in MeanPPH:
    value = i/IntPPH
    IntegratePPH.append(value)
    
#arrayPE500 = np.array(PE500_Final_intensity)   
IntPE500 = integrate.simps(MeanPE500)
IntegratePE500 = []
for i in MeanPE500:
    value = i/IntPE500
    IntegratePE500.append(value)

# arrayPE1000 = np.array(PE1000_Final_intensity)   
IntPE1000 = integrate.simps(MeanPE1000)
IntegratePE1000 = []
for i in MeanPE1000:
    value = i/IntPE1000
    IntegratePE1000.append(value)
    
  
# IntPS = integrate.simps(MeanPS)
# IntegratePS = []
# for i in MeanPS:
#     value = i/IntPS
#     IntegratePS.append(value)

'''ends here'''




         
fig, ax = plt.subplots(dpi = 250)
#graph = ax.bar(Xaxis, Final_intensity,width = 2, yerr=Final_STD, align='center', alpha=1, ecolor='black', capsize=10)
ax.set_ylabel('arbitary unit')
ax.set_xlabel('Different filters (nm)')
ax.set_xticks(Xaxis)
ax.set_title('Intensity of three plastics at 5 mW using 5 different filters')
ax.yaxis.grid(True)
#ax.text(540,0.52,"Power- 178 mW",color="black", fontdict={"fontsize": 10,"ha":"left","va":"center"})
pph =ax.scatter(Xaxis, IntegratePPH, color = 'b')
ax.plot(Xaxis, IntegratePPH, color = 'b')
ax.errorbar(Xaxis, IntegratePPH, yerr = PPH_final_deviation, fmt = '|', color = 'g')

pe500 = ax.scatter(Xaxis, IntegratePE500, color = 'r')
ax.plot(Xaxis, IntegratePE500, color = 'r')
ax.errorbar(Xaxis, IntegratePE500, yerr = PE500_final_deviation, fmt = '|', color = 'y')

pe1000 = ax.scatter(Xaxis, IntegratePE1000, color = 'k')
ax.plot(Xaxis, IntegratePE1000, color = 'k')
ax.errorbar(Xaxis, IntegratePE1000, yerr = PE1000_final_deviation, fmt = '|', color = 'w')

# ps =ax.scatter(Xaxis, IntegratePS, color = 'fuchsia')
# ax.plot(Xaxis, IntegratePS, color = 'fuchsia')
# ax.errorbar(Xaxis, IntegratePS, yerr = PPH_final_deviation, fmt = '|', color = 'k')

# Save the figure and show
#ax.legend((pph, pe500, pe1000), ('PPH', 'PE 500', 'PE 1000'),scatterpoints=1,loc='upper right',
            #ncol=3,fontsize=8)

plt.savefig('Wood intensities.png')
plt.show()

