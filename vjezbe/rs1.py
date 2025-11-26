# 1. 
x = int(input("Unesi broj: "))
interval = [x >=10 and x<50]

print(interval)

# 2. 

import math 

prvi = int(input("Unesi broj: "))
drugi = int(input("Unesi broj: "))
treci = int(input("Unesi broj: "))
cetri = int(input("Unesi broj: "))
peti = int(input("Unesi broj: "))
lista = [prvi, drugi, treci, cetri, peti]

najveci = max(lista)

print(najveci)

# 3. 

student = ("Ana", "Informatika", 22)

print(student[0], student[1], student[2])

# 4. 

def broji_slova(rijec):
    rez = {}
    for s in rijec:
        if s in rez:
            rez[s] +=1
        else:
            rez[s] = 1
    return rez

print(broji_slova("Jabuka"))
