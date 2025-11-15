#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 09:58:57 2025

@author: ofurn
"""

import matplotlib.pyplot as plt

x = ["Toppidrett", "Matte", "Historie", "Kinesisk", "Fysikk", "Prog.", "Norsk"]
y = [5.71, 2.86, 5.36, 0.00, 0.00, 0.00, 2.86]

plt.bar(x, y, color = 'red')
plt.ylabel("Prosent fravær")
plt.xlabel("Fag")
plt.ylim(0, 10)


  