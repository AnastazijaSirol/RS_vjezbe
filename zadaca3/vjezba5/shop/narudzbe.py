from shop.proizvodi import skladiste

class Narudzba:
    def __init__(self, naruceni_proizvodi, ukupna_cijena):
        self.naruceni_proizvodi = naruceni_proizvodi
        self.ukupna_cijena = ukupna_cijena

    def ispis_narudzbe(self):
        opis = ", ".join([f"{p['naziv']} x {p['narucena_kolicina']}" for p in self.naruceni_proizvodi])
        print(f"Naručeni proizvodi: {opis}, Ukupna cijena: {self.ukupna_cijena} EUR")

narudzbe = []

def napravi_narudzbu(naruceni_proizvodi):
    if not isinstance(naruceni_proizvodi, list) or not naruceni_proizvodi:
        print("Greška: naručeni_proizvodi mora biti neprazna lista.")
        return

    for p in naruceni_proizvodi:
        if not isinstance(p, dict) or not all(k in p for k in ["naziv", "cijena", "narucena_kolicina"]):
            print("Greška: svaki proizvod mora biti rječnik s ključevima naziv, cijena i narucena_kolicina.")
            return

        skladisni = next((s for s in skladiste if s.naziv == p["naziv"]), None)
        if not skladisni or skladisni.dostupna_kolicina < p["narucena_kolicina"]:
            print(f"Proizvod {p['naziv']} nije dostupan!")
            return

    for p in naruceni_proizvodi:
        for s in skladiste:
            if s.naziv == p["naziv"]:
                s.dostupna_kolicina -= p["narucena_kolicina"]

    ukupna_cijena = sum(p["cijena"] * p["narucena_kolicina"] for p in naruceni_proizvodi)
    nova = Narudzba(naruceni_proizvodi, ukupna_cijena)
    narudzbe.append(nova)
    return nova
