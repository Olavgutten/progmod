# a

def collatz(n):         # definerer funksjonen
    if n <= 1:
        raise ValueError("Tallet må være større enn 1")

    steg = 0            
    while n != 1:
        if n % 2 == 0:
            n //= 2     # Del på 2 dersom partall
        else:
            n = 3 * n + 1       # 3n + 1 hvis oddetall
        steg += 1
    return steg

n = float(input("Gi et heltall større enn 1: "))
print(f"Det tok {collatz(n)} steg før rekken nådde 1.")


# b

def collatz_steg(n):
    steg = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steg += 1
    return steg

maks_steg = 0
tall_med_maks_steg = 0

for i in range(2, 1000001):
    steg = collatz_steg(i)
    if steg > maks_steg:
        maks_steg = steg
        tall_med_maks_steg = i

print(f"Tallet med lengst kjede under 1 000 000 og over 1 er {tall_med_maks_steg} med {maks_steg} steg.")

# c
# Plotter hvor mange steg i xollatz kjeden, med definisjonsmengde 2-100
import matplotlib.pyplot as plt

def collatz_steg(n):
    """Returnerer antall steg det tar før n når 1 i Collatz-sekvensen."""
    steg = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2       # Del på 2 hvis partall
        else:
            n = 3 * n + 1 # 3n + 1 hvis oddetall
        steg += 1
    return steg

# Lag lister for tallene 2–100 og antall steg for hvert tall
x = list(range(2, 101))
y = [collatz_steg(n) for n in x]

# Lag et pent plott
plt.figure(figsize=(8, 5))
plt.plot(x, y, marker='o', color='black')
plt.title("Antall steg i Collatz-kjeden for starttal mellom 2 og 100")
plt.xlabel("Starttall (n)")
plt.ylabel("Antall steg")
plt.grid(True)
plt.show()

