# 5. 

kvadrat = lambda x: x**2

# 6. 

brojevi = [2, 4, 6, 8]

print(list(map(kvadrat, brojevi)))

# 7. 

L = [3, 10, 7, 8, 12, 5]

parni = lambda x : x%2==0

print(list(filter(parni, L)))

# 8. 

imena = ["Ana", "Marko", "Iva", "Luka"]

tri_slova = [ime for ime in imena if len(ime)==3]

print(tri_slova)

# 9.

class Student:
    def __init__(self, ime, godina, smjer):
        self.ime = ime
        self.godina = godina
        self.smjer = smjer
    def predstavi_se(self):
        print(self.ime, self.godina, self.smjer)