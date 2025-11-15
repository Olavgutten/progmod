#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  3 12:53:51 2025

@author: ofurn
"""

import numpy as np
import random

runder = 1000000

x = np.random.uniform(-1, 1, runder)
y = np.random.uniform(-1, 1, runder)

forholdjobb = x**2 + y**2 < 1
antallstemmer = np.sum(forholdjobb)
sans = (antallstemmer / runder) * 4

print(f"P*4 er lik {sans}")


