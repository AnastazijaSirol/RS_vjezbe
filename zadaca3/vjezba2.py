# 1. 

nizovi = ["jabuka", "kruška", "banana", "naranča"]

print(list(map(lambda x: len(x)**2, nizovi)))

# 2.

brojevi = [1, 21, 33, 45, 2, 2, 1, -32, 9, 10]

print(list(filter(lambda x: x>5, brojevi)))

# 3. 

brojevi = [10, 5, 12, 15, 20]

print(dict(map(lambda x: (x, x**2), brojevi)))

# 4. 

studenti = [
{"ime": "Ivan", "prezime": "Ivić", "godine": 19},
{"ime": "Marko", "prezime": "Marković", "godine": 22},
{"ime": "Ana", "prezime": "Anić", "godine": 21},
{"ime": "Petra", "prezime": "Petrić", "godine": 13},
{"ime": "Iva", "prezime": "Ivić", "godine": 17},
{"ime": "Mate", "prezime": "Matić", "godine": 18}
]

print(all(map(lambda x: x["godine"]>17, studenti)))

# 5. 

rijeci = ["jabuka", "pas", "knjiga", "zvijezda", "prijatelj", "zvuk", "čokolada", "ples",
"pjesma", "otorinolaringolog"]

min_duljina = input("Unesite minimalnu duljinu riječi: ")
min_duljina=int(min_duljina)

duge_rijeci = list(filter(lambda x: len(x)>min_duljina, rijeci))

print(duge_rijeci)