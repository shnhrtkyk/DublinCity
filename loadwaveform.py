#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 08:07:01 2020

@author: shino
"""

import numpy as np
import glob
import scipy

path = "/Volumes/ssd/nyu_2451_38586_las/T_315500_234500/*.txt"
files = []
files = glob.glob(path)
print(files)
maxleng=[]

for file in files:
    with open(file) as f:
        l_strip = [s.strip() for s in f.readlines()]
#        print(l_strip[0].split())
#        print(type(l_strip[0].split()))
    #    l = f.readlines()
    #    print(type(l))
    #    print(l[0])
    length = []
    waves = []
    for line in l_strip:
        line = line.split()
    #    print((line[8]))
    #    print(len(line[9:]))
        if(line[7] != "no_waveform"):
    
            length.append(int(line[2]))
            waves.append(line[7:])
    
    length = np.array(length)
    waves = np.array(waves)
    maxleng.append(np.amax(length))
    print(np.amax(length))
    print(np.amax(waves))
    
print("max is :")
print(np.amax(maxleng))