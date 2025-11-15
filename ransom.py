#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 10:52:29 2025

@author: ofurn
"""

import random as rd

antallforsøk = 100000
riktig = 0

for i in range(antallforsøk):
    x = rd.uniform(-1, 1)
    y = rd.uniform(-1, 1)
    if x**2 + y**2 < 1:
        riktig = riktig + 1

riktig = riktig/1000
        


print(f"På {antallforsøk} runder stemmer påstanden {riktig}% av tilfellene")


        







     