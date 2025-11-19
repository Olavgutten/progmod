#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 10:10:31 2025

@author: ofurn
"""

import numpy as np

# Skal finne f'(1) for alle funksjnene
# f(x)=x**2-4x+5

punkt=1

def f(x):
    return x**2-4*x+5

def deriver(f, punkt, deltaX):
    deltaY = f(punkt+deltaX)-f(punkt)
    return deltaY/deltaX

print(deriver(f, punkt, 10**-4))