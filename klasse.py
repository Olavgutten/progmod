#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 16:21:54 2025

@author: ofurn
"""

# skal lage en klasse glass


# Selve klassen

class Glass:
    def __init__(self, størrelse):
        self.kapasitet = størrelse
        self.innhold = 0
        
    def fyll(self, mengde):
        self.innhold = self.innhold + mengde
        if (self.innhold > self.kapasitet):
            self.innhold = self.kapasitet
            print("Du fylte mer veske enn det er plass til i glasset")
            
    def tøm(self, mengde):
        self.innhold = self.innhold - mengde
        if (self.innhold < 0):
            self.innhold = 0
            print("Glasset er nå tomt")
            
    def sjekkInnhold(self):
        print(f"Det er {self.innhold} dL veske i glasset")
        
    def __eq__(self, other):
        if (self.kapasitet != other.kapasitet):
            return False
        elif (self.innhold != other.innhold):
            return False
        else:
            return True
        
        
        
ass = Glass(2)
ass.sjekkInnhold()
ass.fyll(1.5)
ass.sjekkInnhold()
ass.tøm(10)
ass.sjekkInnhold()
ass.fyll(3)
print(Glass)            
        
            
            
        




