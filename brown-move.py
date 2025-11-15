#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 17:25:52 2025

@author: ofurn
"""

import random
import matplotlib.pyplot as plt

antallsteg = 10000


retninger = ["høyre", "opp", "ned", "venstre"]

y = [0]
x = [0]

for i in range(antallsteg):
    bevegelse = random.choice(retninger)
    if bevegelse == "ned":
        y.append(y[i]-1)
        x.append(x[i])
    if bevegelse == "opp":
        y.append(y[i]+1)
        x.append(x[i])
    if bevegelse == "høyre":
        y.append(y[i])
        x.append(x[i]+1)
    if bevegelse == "venstre":
        y.append(y[i])
        x.append(x[i]-1)
plt.plot(x, y)
plt.show()


    

        
    