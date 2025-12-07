#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  6 12:51:40 2025

@author: ofurn
"""

#Oppgave a)
 # Fikk hjelp av chatGPT til å vite hvordan lese av filene og bruke det
 
 # Oppgave b)
     # Se også tekst i word dokumentet
 
import csv

# Jonas
j_runder = []
j_antall_feil = []
j_tider = []
j_poeng = []
j_handlinger = []  
j_feil = []

with open("JonasPrestasjon.txt", "r") as fil:
    data = csv.DictReader(fil)
    
    for rad in data:
        j_runder.append(float(rad["runder"]))
        j_antall_feil.append(float(rad["feil"]))
        j_tider.append(float(rad["tiderISekund"]))
        j_poeng.append(float(rad["poeng"]))
        j_handlinger.append(float(rad["handlinger"]))
        j_feil.append(float(rad["feil"]))
        
# Per
p_runder = []
p_antall_feil = []
p_tider = []
p_poeng = []
p_handlinger = []
p_feil = []

with open("PerPrestasjon.csv", "r") as fil1:
    data1 = csv.DictReader(fil1)
    
    for rad in data1:
        p_runder.append(float(rad["runder"]))
        p_antall_feil.append(float(rad["feil"]))
        p_tider.append(float(rad["tiderISekund"]))
        p_poeng.append(float(rad["poeng"]))
        p_handlinger.append(float(rad["handlinger"]))
        p_feil.append(float(rad["feil"]))
        

class Spiller:
    
    def __init__(self, person):
        if person == "Jonas":
            self.person = "Jonas"
            self.runder = j_runder
            self.antall_feil = j_antall_feil
            self.tider = j_tider
            self.poeng = j_poeng
            self.feil = j_feil
            self.handlinger = j_handlinger
        elif person == "Per":
            self.person = "Per"
            self.runder = p_runder
            self.antall_feil = p_antall_feil
            self.tider = p_tider
            self.poeng = p_poeng
            self.feil = p_feil
            self.handlinger = p_handlinger
        
    def total_tid(self):
        self.total_tid = sum(self.tider)
        print(self.person, "har spilt totalt", self.total_tid, "sekunder")
        
    def total_poeng(self):
        self.total_poeng = sum(self.poeng)
        print(self.person, "har totalt", self.total_poeng, "poeng")
        
    def total_handlinger(self):
        self.total_handlinger = sum(self.handlinger)
        print(self.person, "har gjort totalt", self.total_handlinger, "handlinger")
        
    def total_feil(self):
        self.total_feil = sum(self.feil)
        print(f"{self.person} har gjort totalt {self.total_feil} feil")
        
    def APM_snitt(self):
        tider_i_minutt = [t / 60 for t in self.tider]
        
        self.apm_liste = [
        handling / tid
        for handling, tid in zip(self.handlinger, tider_i_minutt)
        ]
        # snitt-APM
        apm_snitt = sum(self.apm_liste) / len(self.apm_liste)
        print(f"{self.person} sitt APM-snitt er: {apm_snitt}")
        
        
    def feilrate_snitt(self):
        self.feilrate = [self.feil / self.handlinger for self.feil, self.handlinger
                              in zip(self.feil, self.handlinger)]
        snitt = sum(self.feilrate) / len(self.feilrate)
        print(self.person, "har et feilrate snitt på", snitt)
        
    def poeng_snitt(self):
        poeng_snitt = sum(self.poeng) / len(self.poeng)
        print(self.person, "sitt poengsnitt per runde:", poeng_snitt)
        
    def handling_snitt(self):
        handling_snitt = sum(self.handlinger) / len(self.handlinger)
        print(self.person, "sitt handlingssnitt per runde:", handling_snitt)
        
    def feil_snitt(self):
        feil_snitt = sum(self.feil) / len(self.feil)
        print(self.person, "sitt feilsnitt per runde:", feil_snitt)
        
    def total_runder(self):
        totalerunder = max(self.runder)
        print(self.person, "har spilt totalt", totalerunder, "runder")
        
        
        


# Oppgave b)
    # Se også tekst i word dokumentet
    
per = Spiller("Per")
per.total_tid()
per.total_poeng()
per.total_runder()
per.poeng_snitt()
per.APM_snitt()
per.feilrate_snitt()

jonas = Spiller("Jonas")
jonas.total_tid()
jonas.total_poeng()
jonas.total_runder()
jonas.poeng_snitt()
jonas.APM_snitt()
jonas.feilrate_snitt()

# Plots for visualisering:
    

import matplotlib.pyplot as plt

x = ["Per", "Jonas"]

y = [sum(p_tider), sum(j_tider)]
farger = ["green", "red"]
plt.bar(x, y, color = farger)
plt.xlabel("Navn på spillere")
plt.ylabel("Antall minutter spilt")
plt.title("Jonas og Per totale sekunder spilt")
plt.show()  

y = [sum(p_poeng), sum(j_poeng)]
farger = ["green", "red"]
plt.bar(x, y, color = farger)
plt.xlabel("Navn på spillere")
plt.ylabel("Antall totale poeng")
plt.title("Jonas og Per totale poeng")
plt.show()        
        
y = [max(p_runder), max(j_runder)]
farger = ["green", "red"]
plt.bar(x, y, color = farger)
plt.xlabel("Navn på spillere")
plt.ylabel("Antall totale runder")
plt.title("Jonas og Per totale runder spilt")
plt.show()     

y = [sum(p_poeng) / max(p_runder), sum(j_poeng) / max(j_runder)]
farger = ["green", "red"]
plt.bar(x, y, color = farger)
plt.xlabel("Navn på spillere")
plt.ylabel("Snittpoeng")
plt.title("Jonas og Per snittpoeng per runde")
plt.show()     
   
y = [sum(p_poeng) / max(p_runder), sum(j_poeng) / max(j_runder)]
farger = ["green", "red"]
plt.bar(x, y, color = farger)
plt.xlabel("Navn på spillere")
plt.ylabel("Snittpoeng")
plt.title("Jonas og Per snittpoeng per runde")
plt.show()     
        
y = [87.5636545477869, 81.15322170678057]
farger = ["green", "red"]
plt.bar(x, y, color = farger)
plt.xlabel("Navn på spillere")
plt.ylabel("APM-snitt")
plt.title("Jonas og Per APM-snitt per runde")
plt.show()     

y = [0.09261731548892244, 0.10283681622038877]
farger = ["green", "red"]
plt.bar(x, y, color = farger)
plt.xlabel("Navn på spillere")
plt.ylabel("Feilrate-snitt")
plt.title("Jonas og Per Feilrate-snitt per runde")
plt.show()        


    
# Oppgave c og d
    # Måten jeg gjør numerisk derivasjon her er å ta hver verdi og ta minus den
    # forrige verdien. Da får jeg stigningstallet mellom hvert punkt og dette er
    # den deriverte. Deretter plotter jeg dem og kan se om vi finner noen mistenkelige
    # verdier som skiller seg ut. Vi ser etter steder hvor verdiene endrer seg 
    # mye mer enn det typiske.
    
jonas1 = "red"
per1 = "green"

# Poeng derivert
# per
per_poeng_derivert = []

for i in range(0, 419):
    derivert = p_poeng[i+1] - p_poeng[i]
    per_poeng_derivert.append(derivert)
x = list(range(0, 419))
plt.hist(per_poeng_derivert, bins=30, color = "green")
plt.ylabel("Antall")
plt.xlabel("Deriverte verdier")
plt.title("Poeng derivert for Per")
plt.show()

# jonas

jonas_poeng_derivert = []

for i in range(0, 349):
    derivert = j_poeng[i+1] - j_poeng[i]
    jonas_poeng_derivert.append(derivert)
x = list(range(0, 349))
plt.hist(jonas_poeng_derivert, bins=30, color = "red")
plt.ylabel("Antall")
plt.xlabel("Deriverte verdier")
plt.title("Poeng derivert for Jonas")
plt.show()

# tid derivert
   #per

per_tid_derivert = []

for i in range(0, 419):
    derivert = p_tider[i+1] - p_tider[i]
    per_tid_derivert.append(derivert)
x = list(range(0, 419))
plt.hist(per_tid_derivert, bins=30, color = "green")
plt.ylabel("Antall")
plt.xlabel("Deriverte verdier")
plt.title("Tid derivert for Per")
plt.show()

# jonas

jonas_tid_derivert = []

for i in range(0, 349):
    derivert = j_tider[i+1] - j_tider[i]
    jonas_tid_derivert.append(derivert)
x = list(range(0, 349))
plt.hist(jonas_tid_derivert, bins=30, color = "red")
plt.ylabel("Antall")
plt.xlabel("Deriverte verdier")
plt.title("Tid derivert for Jonas")
plt.show()

#handlinger derivert
# per
per_handlinger_derivert = []

for i in range(0, 419):
    derivert = p_handlinger[i+1] - p_handlinger[i]
    per_handlinger_derivert.append(derivert)
x = list(range(0, 419))
plt.hist(per_handlinger_derivert, bins=30, color = "green")
plt.ylabel("Antall")
plt.xlabel("Deriverte verdier")
plt.title("Handlinger derivert for Per")
plt.show()

# jonas

jonas_handlinger_derivert = []

for i in range(0, 349):
    derivert = j_handlinger[i+1] - j_handlinger[i]
    jonas_handlinger_derivert.append(derivert)
x = list(range(0, 349))
plt.hist(jonas_handlinger_derivert, bins=30, color = "red")
plt.ylabel("Antall")
plt.xlabel("Deriverte verdier")
plt.title("Handlinger derivert for Jonas")
plt.show()

#feil derivert 
# per
per_feil_derivert = []

for i in range(0, 419):
    derivert = p_feil[i+1] - p_feil[i]
    per_feil_derivert.append(derivert)
x = list(range(0, 419))
plt.hist(per_feil_derivert, bins=30, color = "green")
plt.ylabel("Antall")
plt.xlabel("Deriverte verdier")
plt.title("Feil derivert for Per")
plt.show()

# jonas
jonas_feil_derivert = []

for i in range(0, 349):
    derivert = j_feil[i+1] - j_feil[i]
    jonas_feil_derivert.append(derivert)
x = list(range(0, 349))
plt.hist(jonas_feil_derivert, bins=30, color = "red")
plt.ylabel("Antall")
plt.xlabel("Deriverte verdier")
plt.title("Feil derivert for Jonas")
plt.show()


#APM derivert
# per
per_apm_derivert = []

for i in range(0, 419):
    derivert = per.apm_liste[i+1] - per.apm_liste[i]
    per_apm_derivert.append(derivert)
x = list(range(0, 419))
plt.hist(per_apm_derivert, bins=30, color = "green")
plt.ylabel("Antall")
plt.xlabel("Deriverte verdier")
plt.title("APM derivert for Per")
plt.show()

# jonas
jonas_apm_derivert = []

for i in range(0, 349):
    derivert = jonas.apm_liste[i+1] - jonas.apm_liste[i]
    jonas_apm_derivert.append(derivert)
x = list(range(0, 349))
plt.hist(jonas_apm_derivert, bins=30, color = "red")
plt.ylabel("Antall")
plt.xlabel("Deriverte verdier")
plt.title("APM derivert for Jonas")
plt.show()

#feilrate derivert
# per
per_feilrate_derivert = []

for i in range(0, 419):
    derivert = per.feilrate[i+1] - per.feilrate[i]
    per_feilrate_derivert.append(derivert)
x = list(range(0, 419))
plt.hist(per_feilrate_derivert, bins=30, color = "green")
plt.ylabel("Antall")
plt.xlabel("Deriverte verdier")
plt.title("Feilrate derivert for Per")
plt.show()

# jonas
jonas_feilrate_derivert = []

for i in range(0, 349):
    derivert = jonas.feilrate[i+1] - jonas.feilrate[i]
    jonas_feilrate_derivert.append(derivert)
x = list(range(0, 349))
plt.hist(jonas_feilrate_derivert, bins=30, color = "red")
plt.ylabel("Antall")
plt.xlabel("Deriverte verdier")
plt.title("Feilrate derivert for Jonas")
plt.show()

# Kommentar:
    # Den eneste grafen jeg synes ser mistenkelig ut er Poeng derivert for per.
    # Her har han stort sett veldig jevnt derivert så det ligger som oftest nærme
    # 0, men han har én runde som skiller seg veldig ut og her helt oppe mot 2500
    # det kan ha vært en runde han hadde flaks, eller var veldig god, men det kan 
    # også ses på som juks siden den skiller seg veldig ut fra resten.

