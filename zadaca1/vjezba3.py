import random

tajni_broj = random.randint(1, 100)

broj_je_pogoden = False
broj_pokusaja = 0

print("Pogodi broj između 1 i 100!")

while not broj_je_pogoden:
    pretpostavka = int(input("Unesi broj: "))
    broj_pokusaja += 1

    if pretpostavka < tajni_broj:
        print("Traženi broj je veći.")
    elif pretpostavka > tajni_broj:
        print("Traženi broj je manji.")
    else:
        broj_je_pogoden = True
        print(f"Bravo, pogodio si u {broj_pokusaja} pokušaja!")
