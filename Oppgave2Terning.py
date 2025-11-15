# Fyll inn denne filen med egen kode


# a)
# Lag et program som kan simulere 2 terningkast for en tisidet
# terning og anslå P(x > 60)

import random

# Trill to 10-sidede terninger
terning1 = random.randint(1, 10)
terning2 = random.randint(1, 10)

print(f"Terning 1: {terning1}")
print(f"Terning 2: {terning2}")
print(f"Produkt: {terning1 * terning2}")

# Beregn sannsynligheten for at produktet er større enn 60
antall_over_60 = 0
totalt = 0

for terning1 in range(1, 11):
    for terning2 in range(1, 11):
        totalt += 1
        if terning1 * terning2 > 60:
            antall_over_60 += 1

sannsynlighet = antall_over_60 / totalt

print(f"\nSannsynligheten for at produktet er større enn 60 er {sannsynlighet:.2f} ({sannsynlighet*100:.1f}%)")

# b)
# Hva er det minste antall sider på en terning slik at P(x > 60) er større enn 50%

def minste_n():
    for n in range(1, 101):     # prøver terninger med 1–100 sider
        produkt_over_60 = 0
        totalt = n * n          # tar produkt av to terningkast
        for x in range(1, n+1):
            for y in range(1, n+1):
                if x * y > 60:
                    produkt_over_60 += 1
        sannsynlighet = produkt_over_60 / totalt
        if sannsynlighet > 0.5:
            return n, sannsynlighet

n, p = minste_n()
print(f"Minst antall sider for at > 50% sjanse for at produktet > 60 er {n} sider")


