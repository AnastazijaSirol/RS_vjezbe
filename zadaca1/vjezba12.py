def obrni_rjecnik(rjecnik):
    novi_rjecnik = {}
    for kljuc, vrijednost in rjecnik.items():
        novi_rjecnik[vrijednost] = kljuc
    return novi_rjecnik

rjecnik={"a": 1, "b": 2}

print(obrni_rjecnik(rjecnik))
