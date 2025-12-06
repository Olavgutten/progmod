#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 12:35:01 2025

@author: ofurn
"""

# eg skal derivere f(x)= 2*x**2 + x - 5
# numerisk derivasjon vil si at vi bytter ut Δx med et lite tall
# vi får altså en tilnræmet verdi og regner ut gjennomsnittlig vekstfar
# i et veldig lite intervall
# deriver funksjonen

def f(x):
    return 2*x**2 + x - 5

def derivert(f, a, delta_x):
    return (f(a+delta_x)-f(a)) / delta_x

eksakt_verdi = 5

for i in range(1, 17):
    differanse = eksakt_verdi - derivert(f, 1, 10**-i) 
    print(i, derivert(f, 1, 10**-i), differanse)
    
    
    
    


