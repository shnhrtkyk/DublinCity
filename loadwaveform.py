#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 08:07:01 2020

@author: shino
"""

import numpy as np
import glob
import scipy
from dataset import Dataset
from scipy.spatial import ckdtree

path = "/Volumes/ssd/nyu_2451_38586_las/T_315500_234500/*.txt"
files = []
files = glob.glob(path)
print(files)
maxleng=[]

laspath = "/Volumes/ssd/Dublin/*.las"
lasfiles = []
lasfiles = glob.glob(laspath)

#for file in files:
#    with open(file) as f:
#        l_strip = [s.strip() for s in f.readlines()]
#        print(l_strip[0].split())
##        print(type(l_strip[0].split()))
#    #    l = f.readlines()
#    #    print(type(l))
#    #    print(l[0])
#    length = []
#    waves = []
#    for lasfile in lasfiles:
#        ref_ds = Dataset(lasfile)
#        ref_points = ref_ds._xyz
#        out_labels = ref_ds.labels
#        tree = ckdtree.cKDTree(ref_points[:, 0:2])  # only on 2D
#        xyzc_arr = []
#        wave_arr = []
#        for line in l_strip:
#            line = line.split()
##            print((line[8]))
#        #    print(len(line[9:]))
#            if(line[4] != "no_waveform"):
#                xyz = (line[:3])
#                print(xyz)


for lasfile in lasfiles:
    ref_ds = Dataset(lasfile)
    ref_points = ref_ds._xyz
    out_labels = ref_ds.labels
    tree = ckdtree.cKDTree(ref_points[:, 0:2])  # only on 2D
    xyzc_arr = []
    wave_arr = []
    for file in files:
        with open(file) as f:
            l_strip = [s.strip() for s in f.readlines()]
            print(l_strip[0].split())
            print(type(l_strip[0].split()))
        #    l = f.readlines()
        #    print(type(l))
        #    print(l[0])
        length = []
        waves = []
        for line in l_strip:
            line = line.split()
        #    print((line[8]))
        #    print(len(line[9:]))
            if(line[4] != "no_waveform"):
                xyz = (line[:3])
                print(line[:3])
                #lasとマッチング
                multiples = tree.query_ball_point([xyz[0], xyz[1]], r=0.001, eps=0.0001) ## xy
                if(len(multiples)>0):
                    print(multiples)
#                    xyzc_arr.append()
        
                    length.append(int(line[2]))
                    waves.append(line[3:])
        
#        length = np.array(length)
#        waves = np.array(waves)
#        maxleng.append(np.amax(length))
#        print(np.amax(length))
#        print(np.amax(waves))
    
#print("max is :")
#print(np.amax(maxleng))