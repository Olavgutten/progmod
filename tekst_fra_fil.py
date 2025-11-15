#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 22 09:41:20 2025

@author: ofurn
"""

import matplotlib.pyplot as plt

fil = open("temperatur.txt", "r")
fil.readline()

tid = []
temperatur = []
for linje in fil:
    liste = linje.split(",")
    tid.append(int(liste[0]))
    temperatur.append(int(liste[1]))

fil.close()
print(tid)
print(temperatur)    

plt.plot(tid, temperatur)
plt.show()


import numpy as np

data = np.loadtxt("temperatur.txt", skiprows = 1, delimiter = ',')
tid = data[:,0]
temperatur = data[:,1]
plt.plot(tid, temperatur)

plt.show()

import pandas as pd

pingvindata = pd.read_csv("pingviner.txt", delimiter=",")
print(pingvindata.head)

print(pingvindata["bill_depth_mm"])

vekter = pingvindata.sort_values("body_mass_g", ascending=True)

print(vekter)

