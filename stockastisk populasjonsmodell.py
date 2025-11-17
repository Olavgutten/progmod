#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 11:01:29 2025

@author: ofurn
"""

import random
import matplotlib.pyplot as plt

befolkning = 500
levekår = ["dø", "etterkom", "etter"]
randomiser = random.choice(levekår)

for i in range(100):
    if randomiser == "etterkom":
        befolkning = befolkning + 1
    if randomiser == "etter":
        befolkning = befolkning + 1
    if randomiser == "dø":
        befolkning = befolkning -1       



