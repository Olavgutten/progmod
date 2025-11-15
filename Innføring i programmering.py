# 11/45

#5

a = 5

print(a+5*3)

#6

a = 3
b = 2

a = 2
b = 3

print(a+b)

#7

v = 5
a = 9.81
t = 4

print(v+(1/2)*a*t**2)

#8

tall = 56

print(f"Verdien av variabelen tall er {tall}")

#9

a = 11/7

print(f"Svaret på uttrykket blir {a:.3f}")

#10

fornavn = input("Hva er fornavnet ditt?")
   
print(f"Okei, {fornavn} er et veldig fint navn!")

etternavn = input("Men hva er etternavnet ditt?")

print(f"Hyggelig å møte deg {fornavn} {etternavn}. Håper du får en fin dag videre")

#11

tall = input("Skriv et tall mellom 1 og 100")

float_tall = float(tall)

print(f"Du tastet inn {float_tall}")

#12

tall = float(input("Skriv inn et tall:"))

print(f"Du tastet inn {tall}")

#13

heltall = float(input("Skriv inn et heltall:"))

hele_ganger = heltall//5
rest = heltall%5

print(f"Du kan dele {heltall} på fem {hele_ganger} ganger. Resten blir {rest}")

#Eksempel

#A) Areal av et rektangel

l = float(input("Hvor mange meter lang er rektangelet?"))
b = float(input("Okei, hvor mange meter er bredden?"))

print("Rektangelet er", l*b, "kvadratmeter")

#B) Arealet av sirkel

radius = float(input("Hva er radius til sirkelen?"))

print("Arealet på sirkelen er", radius**2*3.14)

#Kondisjoner

##Eksemple

tall = float(input("Skriv et tilfeldig tall"))

if(tall>0):
    print("Tallet er positivt")

elif(tall==0):
    print("Tallet er 0")
    
else:
    print("tallet er negativt")

##Oppgaver slide 25

#1
heltall = float(input("skriv no et tall for fan"))

if(heltall < 5):
    print("Tallet e mindre enn fem")
    
elif(heltall == 5):
    print("tallet e fem")
    
else:
    print("tallet er over 5")
    
#2
destall = float(input("Skriv et desitall"))

if(destall < 0):
    print("True")
    
else:
    print("False")
      
#3
tall1 = float(input("Skriv et tall"))

tall2 = float(input("Skriv et tall til"))

if(tall1 == tall2):
    print("True")
    
else:
    print("False")
    
#4
rantall = float(input("Gje meg et tall"))

if(rantall%2 == 0):
    print("Partall")

else:
    print("Oddetall")
    

    
    


























































