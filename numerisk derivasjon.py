#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 09:43:39 2025

@author: ofurn
"""

import numpy as np

def f(x):
    return 2*x**2+x-5

def deriver(funksjon, punkt, deltaX):
    deltaY = funksjon(punkt+deltaX)-funksjon(punkt)
    return deltaY/deltaX
    
  
print(deriver(f, 1, 10**-4))

# Feilanalyse

punkt = 1
def fDerivAna(x):
    return 4*x+1

for i in range(1, 16):
    deltaX = 10**-i
    fDerivApproks = deriver(f,punkt,deltaX)
    feilProsent = abs(fDerivApproks-fDerivAna(punkt))/fDerivAna(punkt)*100
    
    print(f"Når deltaX er {deltaX} så er feilen {feilProsent}%")
    
    
    