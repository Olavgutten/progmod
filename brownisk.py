#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 10:40:05 2025

@author: ofurn
"""

import random as rd
import matplotlib.pyplot as plt

y = [0]
x = [0]

retninger = ["høyre", "venstre", "opp", "ned"]
antallsteg = 1000
retning = rd.choice(retninger)

for i in range(antallsteg):
    if retning == "høyre":
        x.append(x[i]+1)
        y.append(y[i])
    if retning == "ned":
        y.append(y[i]-1)
        x.append(x[i])
    if retning == "opp":
        y.append(y[i]+1)
        x.append(x[i])
    if retning == "venstre":
        x.append(x[i]-1)
        y.append(y[i])
        
plt.plot(x,y)
plt.show()       


print(retning)