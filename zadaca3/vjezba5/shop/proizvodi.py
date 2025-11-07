class Proizvod:
    def __init__(self, naziv, cijena, dostupna_kolicina):
        self.naziv = naziv
        self.cijena = cijena
        self.dostupna_kolicina = dostupna_kolicina

    def ispis(self):
        print(f"Naziv: {self.naziv}, Cijena: {self.cijena} EUR, Dostupno: {self.dostupna_kolicina} kom")

skladiste = [
    Proizvod("Laptop", 5000, 10),
    Proizvod("Monitor", 1500, 20)
]

def dodaj_proizvod(naziv, cijena, dostupna_kolicina):
    novi = Proizvod(naziv, cijena, dostupna_kolicina)
    skladiste.append(novi)
