#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 22:09:30 2025

@author: ofurn
"""

# nå lage en klasse for telefon



class menneske:
    
    def __init__(self, navn):
        self.navn = navn
        self.poeng = 0
    
    def religion(self, religion):
        if religion == "kristen":
            self.poeng = self.poeng + 1
        elif religion == "jøde":
            self.poeng = self.poeng + 10
        else:
            print("Uffa meg. Vi må desverre trekke deg -1 poeng for å være", religion, "og ikke kristen eller jøde")
            self.poeng = self.poeng - 1
            
    def hudfarge(self, hudfarge):
        if hudfarge == "hvit":
            print("+1 poeng for å være hvit")
            self.poeng = self.poeng + 1
        else:
            print("-1 poeng for å være", hudfarge, "og ikke hvit")
            self.poeng = self.poeng - 1
            
    def sjekkpoeng(self):
        print("Du har", self.poeng, "poeng totalt")
        


navn = input("Heisann hva heter du?")

p1 = menneske(navn)

p1.hudfarge(input(f"Hyggelig å møte deg {navn}, men hvilke hudfarge har du?"))

p1.religion(input("Anyways. Jeg har et til spørsmål til deg: Hvilke religion tilhører du?"))

p1.sjekkpoeng()










            
            
            