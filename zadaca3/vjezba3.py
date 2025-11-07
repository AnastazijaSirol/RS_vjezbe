# 1. 

parni_kvadrati = [x**2 for x in range(20, 51) if (x**2) % 2 == 0]

print(parni_kvadrati)

# 2.

rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
"pjesma", "otorinolaringolog"]

duljina_nizova = [len(x) for x in rijeci if "a" in x]

print(duljina_nizova)

# 3. 

kubovi = [{x: x**3 if x % 2 != 0 else x} for x in range(1, 11)]

print(kubovi)

# 4.
import math

korijeni = {x: round(math.sqrt(x), 2) for x in range(50, 501, 50)}

print(korijeni)

# 5.

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "bodovi": [12, 23, 53, 64]},
    {"ime": "Marko", "prezime": "Marković", "bodovi": [33, 15, 34, 45]},
    {"ime": "Ana", "prezime": "Anić", "bodovi": [8, 9, 4, 23, 11]},
    {"ime": "Petra", "prezime": "Petrić", "bodovi": [87, 56, 77, 44, 98]},
    {"ime": "Iva", "prezime": "Ivić", "bodovi": [23, 45, 67, 89, 12]},
    {"ime": "Mate", "prezime": "Matić", "bodovi": [75, 34, 56, 78, 23]}
]

zbrojeni = [{s["prezime"]: sum(s["bodovi"])} for s in studenti]

print(zbrojeni)

# 6. 

faktorijeli = {x: [math.factorial(x)] for x in range(1, 11)}
print(faktorijeli)