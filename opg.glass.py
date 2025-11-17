#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 11:17:36 2025

@author: ofurn
"""

class glass:
    
    def __init__(self, størrelse):
        self.kapasitet = størrelse
        self.innhold = 0
        
    def fyll(self, mengde):
        self.innhold = self.innhold + mengde
        if self.innhold > self.kapasitet:
            print("Du fylte for mye i glasset det ble søl")
    
    def tøm(self, mengde):
        self.innhold = self.innhold - mengde
        if mengde >= self.innhold:
            print("Nå er glasset tomt")
            
    def sjekk(self):
        print(f"Det er {self.innhold} dl igjen i glasset")

glass = glass(5)
glass.fyll(5)
glass.tøm(4)
glass.sjekk()

    