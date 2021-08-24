# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 14:21:24 2020

@author: Admin
"""
from pyueye import ueye
import time
import cv2
import numpy as np
from collections import Counter

# import sys
# sys.path.insert(1, 'F:\Multispectral Imaging\Stepper Motor')

# from stepper_motor import Arduino
ffname='bg_200ms'
    
def main():
    # init camera
    hcam = ueye.HIDS(0)
    ret = ueye.is_InitCamera(hcam, None)
    print(f"initCamera returns {ret}")
    
    # set color mode
    ret = ueye.is_SetColorMode(hcam, ueye.IS_CM_RGB8_PACKED)
    print(f"SetColorMode IS_CM_BGRA8_Packed returns {ret}")
    
    # set region of interest
    width = 1936
    height = 1216
    rect_aoi = ueye.IS_RECT()
    rect_aoi.s32X = ueye.int(0)
    rect_aoi.s32Y = ueye.int(0)
    rect_aoi.s32Width = ueye.int(width)
    rect_aoi.s32Height = ueye.int(height)
    ueye.is_AOI(hcam, ueye.IS_AOI_IMAGE_SET_AOI, rect_aoi, ueye.sizeof(rect_aoi))
    print(f"AOI IS_AOI_IMAGE_SET_AOI returns {ret}")
    
    
    #Auto parameter is disbaled
    auto = ueye.double(0)
    auto1 = ueye.double(0)
    speed = ueye.double(50)
    auto_parameter = ueye.is_SetAutoParameter (hcam, ueye.IS_SET_ENABLE_AUTO_GAIN, auto, auto1)
    auto_parameter1 = ueye.is_SetAutoParameter ( hcam, ueye.IS_SET_ENABLE_AUTO_SHUTTER, auto, auto1)
    auto_parameter2 = ueye.is_SetAutoParameter ( hcam, ueye.IS_SET_ENABLE_AUTO_FRAMERATE, auto, auto1)
    auto_parameter3 = ueye.is_SetAutoParameter ( hcam, ueye.IS_SET_AUTO_BRIGHTNESS_ONCE, auto, auto1)
    auto_parameter4 = ueye.is_SetAutoParameter ( hcam, ueye.IS_SET_AUTO_SPEED, speed, auto1)
    auto_parameter5 = ueye.is_SetAutoParameter ( hcam, ueye.IS_SET_AUTO_SKIPFRAMES, auto, auto1)
    auto_parameter6 = ueye.is_SetAutoParameter ( hcam, ueye.IS_SET_AUTO_HYSTERESIS, auto, auto1)
    
    print(f"auto_paramter returns: {auto_parameter}")
    print(f"auto_paramter1 returns: {auto_parameter1}")
    print(f"auto_paramter2 returns: {auto_parameter2}")
    print(f"auto_paramter3 returns: {auto_parameter3}")
    print(f"auto_paramter4 returns: {auto_parameter4}")
    print(f"auto_paramter5 returns: {auto_parameter5}")
    print(f"auto_paramter6 returns: {auto_parameter6}")
    
       
    # pixel clock is set
    pixel_clock = ueye.uint(30)
    get_pixel_clock = ueye.is_PixelClock(hcam, ueye.IS_PIXELCLOCK_CMD_SET, pixel_clock, ueye.sizeof(pixel_clock))
    print(f"pixel clock returns {get_pixel_clock}")

    # Frame rate is set
    newFPS = ueye.double(0)
    frame_rate = ueye.is_SetFrameRate (hcam, 2.00 , newFPS)
    print(f"frame rate returns: {frame_rate}")

    #Exposure time is set
    exposure_parameter = ueye.double(200)
    exposure = ueye.is_Exposure (hcam,ueye.IS_EXPOSURE_CMD_SET_EXPOSURE, exposure_parameter, ueye.sizeof(exposure_parameter))
    print(f"exposure time returns: {exposure}")
    
    # Binning setting
    binning = ueye.is_SetBinning (hcam, ueye.IS_BINNING_DISABLE)
    print(f"binning returns: {binning}")
    
    #Gain mode is set
    gain_mode = ueye.is_SetGainBoost (hcam, ueye.IS_SET_GAINBOOST_OFF)
    print(f"gain_mode returns: {gain_mode}")
    
    gain_hardware_mode = ueye.is_SetHardwareGain (hcam, 100, ueye.IS_IGNORE_PARAMETER, ueye.IS_IGNORE_PARAMETER, ueye.IS_IGNORE_PARAMETER)
    print(f"gain_hardware_mode: {gain_hardware_mode}")
    
    # Gamma correction
    gamma = ueye.int()
    gamma_correction = ueye.is_Gamma(hcam, ueye.IS_GAMMA_CMD_GET_DEFAULT , gamma, ueye.sizeof(gamma))
    print(f"gamma_correction returns: {gamma_correction}")
    
    #Hot pixel correction
    hot = ueye.int(0)
    hot_pixel = ueye.is_HotPixel (hcam, ueye.IS_HOTPIXEL_ENABLE_CAMERA_CORRECTION, hot, ueye.sizeof(hot) )
    print(f"hot_pixel returns: {hot_pixel}")
    
    #Saturation is set
    saturationU = ueye.int(50)
    saturationV = ueye.int(50)
    set_saturation = ueye.is_SetSaturation (hcam, saturationU, saturationV)
    print(set_saturation)
    
    #edege detection
    edge = ueye.int(9)
    Edge=ueye.is_EdgeEnhancement(hcam, ueye.IS_EDGE_ENHANCEMENT_CMD_SET, edge , ueye.sizeof(edge))
    print(f"edge {Edge}")                        
    # ard = Arduino('COM10')
       
    for i in range(2):     
        #ard.query('2'
        #time.sleep(3)
        filters = [440, 460, 500, 560, 610]
        print("------------------")
        
        mem_ptr = ueye.c_mem_p()
        mem_id = ueye.int()
        bitspixel = 24
        ret = ueye.is_AllocImageMem(hcam, width, height, bitspixel,
                                    mem_ptr, mem_id)
        print(f"AllocImageMem returns {ret}")
            
        # set active memory region
        ret = ueye.is_SetImageMem(hcam, mem_ptr, mem_id)
        print(f"SetImageMem returns {ret}")
        FileParams = ueye.IMAGE_FILE_PARAMS()
        FileParams.pwchFileName = f"{ffname}_{i}.png"
        FileParams.nFileType = ueye.IS_IMG_PNG
        FileParams.nQuality = 100
        FileParams.ppcImageMem = None
        FileParams.pnImageID = None
            
        # trigger = ueye.is_SetExternalTrigger(hcam, ueye.IS_SET_TRIGGER_SOFTWARE)
        # print(f"trigger: {trigger}")
                        
        ret = ueye.is_FreezeVideo(hcam, ueye.IS_WAIT)
        print(f"return : {ret}")
        print(f"Image capture returns {i}")
        
        
                   
        nret = ueye.is_ImageFile(hcam, ueye.IS_IMAGE_FILE_CMD_SAVE, FileParams, ueye.sizeof(FileParams))
        print('save image',nret)
        # ret = ueye.is_StopLiveVideo(hcam, ueye.IS_FORCE_VIDEO_STOP)
        # print(f"StopLiveVideo returns {ret}")
        free = ueye.is_FreeImageMem (hcam, mem_ptr, mem_id )
        print(f"free: {free}")
        print("------------------------")
    ueye.is_ExitCamera(hcam)
    
    Z = cv2.imread('F:\Multispectral Imaging\Camera codes\Final codes/'+ ffname +'_'+str(i)+'.png', 1)
    #Z= Z[:,:, 0]
    
    #max1 = np.argmax(Z)
    print(np.argmax(Z))
    max2 = np.mean(Z)
    #print(Counter(Z))
    #Z = Z[Z < 245]
    max3 = np.max(Z)
    #print(Z.split()[0])
    #max_8bit = (max2 *255)/65536
    print("mean: "+ str(max2))
    print("max: "+ str(max3))
    #print("max_8_bit:", max_8bit)
    #row, col = (np.argmax(Z)//Z.shape[1],  np.argmax(Z)%Z.shape[1])
    #print(row, col)
    
    
if __name__ == '__main__':
    main()




