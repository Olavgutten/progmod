#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 13:37:52 2025

@author: ofurn
"""


# Oppgave a)
print("Oppgave a)")

def f(x):
    return 3*x**3 - 2*x**2 + 5*x - 7

x = 1

def g(x, delta_x):
    return (f(x + delta_x) - f(x - delta_x)) / (2*delta_x)

delta_x = 1E-7

print("Den deriverte med sentraldifferansen er tilnærmet lik:", g(x, delta_x))
print("")
# Oppgave b)
print("Oppgave b)")

def r(x):
    return (4 * g(x, delta_x/2) - g(x, delta_x)) / 3

print("Den deriverte med Richardson ekstrapolasjon er tilnærmet lik", r(x))

# Oppgave c)
    # Resultat fra testingen ligger i word dokument
print("")

# Oppgave d)
print("Oppgave d)")

import math  # Jeg brukte chatGPT for hvordan jeg skulle bruke math

def a(x):
    return x * math.exp(x)

fasit = 5.436563656 # Brukte CAS til å finne den deriverte i x = 1

def prosentvis_feil(verdi, fasit):
    return abs(((verdi - fasit) / fasit) * 100)

# Sentraldifferanse

prosentfeil_s = []

def b(x, delta_x):
    return (a(x + delta_x) - a(x - delta_x)) / (2*delta_x)

for i in range(0, 15):
    delta_x = 10**-i
    prosent = prosentvis_feil(b(1, delta_x), fasit)
    prosentfeil_s.append(prosent)
    

# Richardson ekstrapolasjon

prosentfeil_r = []

def R(x, delta_x):
    return (4 * b(x, delta_x/2) - b(x, delta_x)) / 3

for i in range(0, 15):
    delta_x = 10**-i
    prosent = prosentvis_feil(R(1, delta_x), fasit)
    prosentfeil_r.append(prosent)
    
# Finne lavest prosentvis feil:
    # Her fikk jeg hjelp av chatGPT til å finne ut hvordan bruke liste.index().
    
minste_s = min(prosentfeil_s)
posisjon = prosentfeil_s.index(minste_s)

print("Beste delta_x for sentraldifferansen er:", 10**-posisjon)

minste_r = min(prosentfeil_r)
pos = prosentfeil_r.index(minste_r)

print("Beste delta_x for Richardson ekstrapolasjon er:", 10**-pos)

# Her under er algoritmene oppdatert til å ha ny delta_x verdi som gir lavest
# prosentvis feil fra fasit:
    
delta_x_s = 10**-posisjon

print("Sentraldifferanse med oppdatert delta_x verdi:", b(x, delta_x_s))

best_delta_x_r = 10**-pos

print("Richardson med oppdatert delta_x verdi", R(x, best_delta_x_r))

print("")

# Oppgave e)
print("Oppgave e)")

x = 0.35

def e(x):
    return 5*x*math.exp(-2*x)

def z(x, delta_x):
    return (e(x + delta_x_s) - e(x - delta_x_s)) / (2*delta_x_s)

def q(x):
    return (4 *z(x, best_delta_x_r/2) - z(x, best_delta_x_r)) / 3
    
print("Den deriverte i punktet x = 0.35 er tilnærmet lik:", q(x))



   





        




