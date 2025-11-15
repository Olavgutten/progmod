#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 11:27:12 2025

@author: ofurn
"""

import random
import matplotlib.pyplot as plt

y=[0]
x=[0]

muligretning = ["opp", "ned", "venstre", "høyre"]
antallsteg = 10

for i in range(antallsteg):
    retning = random.choice(muligretning)
    if retning == "opp":
        x.append(x[i])
        y.append(y[i]+1)
    if retning == "ned":
        x.append(x[i])
        y.append(y[i]-1)
    if retning == "høyre":
        x.append(x[i]+1)
        y.append(y[i])
    if retning == "venstre":
        x.append(x[i]-1)
        y.append(y[i])
        
plt.plot(x,y)
plt.plot(x[0],y[0], marker="o", color="green")
plt.plot(x[antallsteg-1], y[antallsteg-1], marker="o",color="red")
plt.show()



        