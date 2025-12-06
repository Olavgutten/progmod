#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 30 15:46:28 2025

@author: ofurn
"""

# eg vil lage en klasse for å lade telefonen

class telefon:
    def __init__(self, batteri):
        self.kapasitet = batteri
        self.innhold = 0
        
    def lade(self, antprosent):
        self.oppladet = self.innhold + antprosent
        if self.oppladet >= self.kapasitet:
            print("Nå er mobilen fulladet")
            
    def tøm(self, antprosent):
        self.strøm = self.innhold - antprosent
        if self.strøm < self.innhold:
            print("Mobilen er tom for strøm")
            
    def sjekkStrøm(self):
        print(f"Det er {self.innhold}% igjen i telefonen")
        








    
    





    


