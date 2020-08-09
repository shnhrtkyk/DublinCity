#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 13:04:54 2020

@author: shino
"""
import numpy as np
import os
import glob


path = "/Users/shino/Downloads/Dublin/*.txt"
files = []
files = glob.glob(path)
print(files)
rgb_pre = np.zeros(3, dtype=np.int)

bulding = [0, 85, 255]
window = [0, 255, 255]
wall = [170, 0, 255]
bush = [170, 255, 127]
walk = [255, 170, 0]
road = [170, 0, 0]
veg = [0, 170, 0]
undef = [255, 255, 127]

mask_mapping = {
    (0, 85, 255):   0,
    (0, 255, 255):   1,
    (170, 0, 255): 2,
    (170, 255, 127):   3,
    (255, 170, 0): 4,
    (170, 0, 0):   5,
    (0, 170, 0): 6,
    (255, 255, 127):   7,
}

count = np.zeros(8, dtype=np.int) 

for file in files:
    print(file)
    data = np.loadtxt(file, skiprows = 1, usecols = (0,1,2,3,4,5))
    savelabel = np.zeros(data.shape[0], dtype=np.int)
    
    print(savelabel.shape)
    
    
    idx =0
    rgb = np.zeros(3, dtype=np.int)
    
    for line in data:
        
        rgb[0] = line[3]
        rgb[1] = line[4]
        rgb[2] = line[5]
    
        if(bulding[0]== rgb[0] and bulding[1]== rgb[1] and bulding[2]== rgb[2]):
            savelabel[idx] = 0
            count[0] += 1
            print("Build")
        elif(window[0]== rgb[0] and window[1]== rgb[1] and window[2]== rgb[2]):
            savelabel[idx] = 1      
            count[1] += 1
            print("window")
        elif(wall[0]== rgb[0] and wall[1]== rgb[1] and wall[2]== rgb[2]):
            savelabel[idx] = 2  
            count[2] += 1
        elif(bush[0]== rgb[0] and bush[1]== rgb[1] and bush[2]== rgb[2]):
            savelabel[idx] = 3
            count[3] += 1
        elif(walk[0]== rgb[0] and walk[1]== rgb[1] and walk[2]== rgb[2]):
            savelabel[idx] = 4
            count[4] += 1
        elif(road[0]== rgb[0] and road[1]== rgb[1] and road[2]== rgb[2]):
            savelabel[idx] = 5    
            count[5] += 1
        elif(veg[0]== rgb[0] and veg[1]== rgb[1] and veg[2]== rgb[2]):
            savelabel[idx] = 6    
            count[6] += 1
        elif(undef[0]== rgb[0] and undef[1]== rgb[1] and undef[2]== rgb[2]):
            savelabel[idx] = 7
            count[7] += 1
            
        idx+=1
    
#    print(count)
#    print(data.shape)
#    print(savelabel.shape)
    data[:,3] = savelabel
#    print(data.shape)
    np.savetxt(file.replace(".txt", "_class.txt"), data[:,:4])
#    if(rgb[0]== rgb_pre[0] and rgb[1]== rgb_pre[1] and rgb[2]== rgb_pre[2]):
#        a =0
#    else:
#        rgb_pre = rgb
#        
#        print(rgb)







