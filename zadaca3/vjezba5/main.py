from shop import proizvodi
from shop import narudzbe

novi_proizvodi = [
    ("Tipkovnica", 300, 20),
    ("Miš", 200, 30),
    ("USB stick", 100, 50),
    ("Punjač", 150, 25)
]

for naziv, cijena, kolicina in novi_proizvodi:
    proizvodi.dodaj_proizvod(naziv, cijena, kolicina)

print("Skladište:")
for p in proizvodi.skladiste:
    p.ispis()

naruceni = [
    {"naziv": "Laptop", "cijena": 5000, "narucena_kolicina": 2},
    {"naziv": "Monitor", "cijena": 1500, "narucena_kolicina": 1}
]

print("\nNarudžba:")
narudzba = narudzbe.napravi_narudzbu(naruceni)
if narudzba:
    narudzba.ispis_narudzbe()
