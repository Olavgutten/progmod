#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  7 11:10:28 2025

@author: ofurn
"""

import random
import matplotlib.pyplot as plt

# Oppgave a)

x = [0]
y = [1]

mulige_utfall = ["smitte", "ikke_smitte"]
sannsynlighet = [0.60, 0.40] # 60% sjanse for å smitte videre, 40% for å ikke
utfall = random.choices(mulige_utfall, weights=sannsynlighet, k=1)[0]

if utfall == "smitte":
    smittede = sum(y) * 5 # Smitter 5 personer av gangen
    y.append(smittede)
    print(y)
    x.append(1)
    
    
else:
    x.append(1)
    y.append(1)
    print("Ingen ble smittet")
    
plt.plot(x, y)
plt.title("Utvikling i antall smittede")
plt.xlabel("Dager")
plt.ylabel("Antall smittede")
plt.show()


# Oppgave b)

N = 100
p = 0.1
k = 5
d = 7

smittede = [1]
smittbare = [99]
restituert = [0]

x = list(range(0, 31))


for dager in range(0, 30):
    prob_utfall = ["smitte", "ikke_smitte"]
    sanns = [p, 0.90]
    utf = random.choices(prob_utfall, weights=sanns, k=1)[0]
    
    ny_smittede = smittede[-1]
    ny_smittbare = smittbare[-1]
    ny_restituert = restituert[-1]
    
    if len(smittede) > d:
        if smittede[-8] > 1:
            ny_restituert = smittede[-8]
            ny_smittede = ny_smittede - smittede[-8]
    
    if utf == "smitte":
        ny_smittede = smittede[-1] + k
        ny_smittbare = smittbare[-1] - k
    
    smittede.append(ny_smittede)
    smittbare.append(ny_smittbare)
    restituert.append(ny_restituert)

blå = "blue"
grønn = "green"
rød = "red"

plt.plot(x, smittede, label = "utvikling av smittede", color = rød)
plt.plot(x, smittbare, label = "utvikling av smittbare", color = grønn)
plt.plot(x, restituert, label = "utvikling av restituerte", color = blå)     
plt.title("Utviklingen til smittbare, restituerte og smittede i befolkningen")
plt.xlabel("Dager")
plt.ylabel("Antall folk")
plt.legend() # Jeg fikk ikke til å få opp navn på linjene så brukte KI hjelp med legend()
plt.show()






        
        
        

    