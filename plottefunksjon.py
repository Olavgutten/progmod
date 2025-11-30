#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 15:46:28 2025

@author: ofurn
"""

# oppgave til siste lside i innføring programmering

import matplotlib.pyplot as plt
def f(x):
    return (1-2*x) / (x-2)
x = 8
y = []
b = []
while x >= -8:
    if(x != 2):
        print(x, f(x))  
        y.append(f(x))
        b.append(x)
    x = x - 1
x = b
plt.plot(x, y)
plt.show()







    
    





    


