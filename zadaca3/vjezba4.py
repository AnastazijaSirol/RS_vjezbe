from datetime import datetime

# 1. 

class Automobil:
    def __init__(self, marka, model, godina_proizvodnje, kilometraza):
        self.marka = marka
        self.model = model
        self.godina_proizvodnje = godina_proizvodnje
        self.kilometraza = kilometraza

    def ispis(self):
        print(f"Marka: {self.marka}")
        print(f"Model: {self.model}")
        print(f"Godina proizvodnje: {self.godina_proizvodnje}")
        print(f"Kilometraža: {self.kilometraza} km")

    def starost(self):
        trenutna_godina = datetime.now().year
        starost = trenutna_godina - self.godina_proizvodnje
        print(f"Automobil je star {starost} godina.")

auto = Automobil("Toyota", "Corolla", 2015, 120000)

auto.ispis()
auto.starost()

# 2. 

import math

class Kalkulator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def zbroj(self):
        return self.a + self.b

    def oduzimanje(self):
        return self.a - self.b

    def mnozenje(self):
        return self.a * self.b

    def dijeljenje(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Greška: dijeljenje s nulom nije dozvoljeno."

    def potenciranje(self):
        return self.a ** self.b

    def korijen(self):
        korijeni = {}
        korijeni['a'] = math.sqrt(self.a) if self.a >= 0 else "Negativan broj"
        korijeni['b'] = math.sqrt(self.b) if self.b >= 0 else "Negativan broj"
        return korijeni

brojevi = Kalkulator(16, 4)

print("Zbroj:", brojevi.zbroj())
print("Oduzimanje:", brojevi.oduzimanje())
print("Množenje:", brojevi.mnozenje())
print("Dijeljenje:", brojevi.dijeljenje())
print("Potenciranje:", brojevi.potenciranje())
print("Korijeni:", brojevi.korijen())

# 3.

class Student:
    def __init__(self, ime, prezime, godine, ocjene):
        self.ime = ime
        self.prezime = prezime
        self.godine = godine
        self.ocjene = ocjene

    def prosjek(self):
        return sum(self.ocjene) / len(self.ocjene) if self.ocjene else 0

studenti = [
    {"ime": "Ivan", "prezime": "Ivić", "godine": 19, "ocjene": [5, 4, 3, 5, 2]},
    {"ime": "Marko", "prezime": "Marković", "godine": 22, "ocjene": [3, 4, 5, 2, 3]},
    {"ime": "Ana", "prezime": "Anić", "godine": 21, "ocjene": [5, 5, 5, 5, 5]},
    {"ime": "Petra", "prezime": "Petrić", "godine": 13, "ocjene": [2, 3, 2, 4, 3]},
    {"ime": "Iva", "prezime": "Ivić", "godine": 17, "ocjene": [4, 4, 4, 3, 5]},
    {"ime": "Mate", "prezime": "Matić", "godine": 18, "ocjene": [5, 5, 5, 5, 5]}
]

studenti_objekti = [Student(s["ime"], s["prezime"], s["godine"], s["ocjene"]) for s in studenti]

najbolji_student = max(studenti_objekti, key=lambda s: s.prosjek())

print(f"Najbolji student: {najbolji_student.ime} {najbolji_student.prezime} s prosjekom {najbolji_student.prosjek()}")

# 4.

class Krug:
    def __init__(self, r):
        self.r = r

    def opseg(self):
        return 2 * math.pi * self.r

    def povrsina(self):
        return math.pi * self.r ** 2

krug = Krug(5)

# Ispis rezultata
print(f"Opseg kruga: {krug.opseg():.2f}")
print(f"Površina kruga: {krug.povrsina():.2f}")

# 5.

class Radnik:
    def __init__(self, ime, pozicija, placa):
        self.ime = ime
        self.pozicija = pozicija
        self.placa = placa

    def work(self):
        print(f"Radim na poziciji {self.pozicija}.")

class Manager(Radnik):
    def __init__(self, ime, pozicija, placa, department):
        super().__init__(ime, pozicija, placa)
        self.department = department

    def work(self):
        print(f"Radim na poziciji {self.pozicija} u odjelu {self.department}.")

    def give_raise(self, radnik, povecanje):
        radnik.placa += povecanje
        print(f"{radnik.ime} je dobio povišicu. Nova plaća: {radnik.placa} EUR")

radnik1 = Radnik("Ivan", "Programer", 1200)
manager1 = Manager("Ana", "Voditelj tima", 2000, "Razvoj")

radnik1.work()
manager1.work()
manager1.give_raise(radnik1, 300)
