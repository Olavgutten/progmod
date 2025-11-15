#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 09:36:02 2025

@author: ofurn
"""

import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 3, 5, 10]
y = [2, 4, 7, 9, 20]

plt.plot(x, y, color = 'red', linestyle = '- -', linewidth = 4)
plt.title("Mitt plott")
plt.xlabel("X-verdier")
plt.ylabel("Y-verdier")

plt.show()


def f(x):
    return 2*x**2 - 2*x +1

x = np.li