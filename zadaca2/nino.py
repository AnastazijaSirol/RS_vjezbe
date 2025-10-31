pozivni_brojevi = [
    {
        "01": {
            "mjesto": "Grad Zagreb i Zagrebačka županija",
            "vrsta": "Fiksna mreža"
        }
    },
    {
        "020": {
            "mjesto": "Dubrovačko-neretvanska županija",
            "vrsta": "Fiksna mreža"
        }
    },
    {
        "021": {
            "mjesto": "Splitsko-dalmatinska županija",
            "vrsta": "Fiksna mreža"
        }
    },
    {
        "022": {
            "mjesto": "Šibensko-kninska županija",
            "vrsta": "Fiksna mreža"
        }
    },
    {
        "023": {
            "mjesto": "Zadarska županija",
            "vrsta": "Fiksna mreža"
        }
    },
    {
        "031": {
            "mjesto": "Osječko-baranjska županija",
            "vrsta": "Fiksna mreža"
        }
    },
    {
        "032": {
            "mjesto": "Vukovarsko-srijemska županija",
            "vrsta": "Fiksna mreža"
        }
    },
    {
        "033": {
            "mjesto": "Virovitičko-podravska županija",
            "vrsta": "Fiksna mreža"
        }
    },
    {
        "034": {
            "mjesto": "Požeško-slavonska županija",
            "vrsta": "Fiksna mreža"
        }
    },
    {
        "035": {
            "mjesto": "Brodsko-posavska županija",
            "vrsta": "Fiksna mreža"
        }
    },
    {
        "040": {
            "mjesto": "Međimurska županija",
            "vrsta": "Fiksna mreža"
        }
    },
    {
        "042": {
            "mjesto": "Varaždinska županija",
            "vrsta": "Fiksna mreža"
        }
    },
    {
        "043": {
            "mjesto": "Bjelovarsko-bilogorska županija",
            "vrsta": "Fiksna mreža"
        }
    },
    {
        "044": {
            "mjesto": "Sisačko-moslavačka županija",
            "vrsta": "Fiksna mreža"
        }
    },
    {
        "047": {
            "mjesto": "Karlovačka županija",
            "vrsta": "Fiksna mreža"
        }
    },
    {
        "048": {
            "mjesto": "Koprivničko-križevačka županija",
            "vrsta": "Fiksna mreža"
        }
    },
    {
        "049": {
            "mjesto": "Krapinsko-zagorska županija",
            "vrsta": "Fiksna mreža"
        }
    },
    {
        "051": {
            "mjesto": "Primorsko-goranska županija",
            "vrsta": "Fiksna mreža"
        }
    },
    {
        "052": {
            "mjesto": "Istarska županija",
            "vrsta": "Fiksna mreža"
        }
    },
    {
        "053": {
            "mjesto": "Ličko-senjska županija",
            "vrsta": "Fiksna mreža"
        }
    },
    {
        "091": {
            "mjesto": "A1 Hrvatska",
            "vrsta": "Mobilna mreža"
        }
    },
    {
        "092": {
            "mjesto": "Tomato",
            "vrsta": "Mobilna mreža"
        }
    },
    {
        "095": {
            "mjesto": "Telemach",
            "vrsta": "Mobilna mreža"
        }
    },
    {
        "097": {
            "mjesto": "bonbon",
            "vrsta": "Mobilna mreža"
        }
    },
    {
        "098": {
            "mjesto": "Hrvatski Telekom",
            "vrsta": "Mobilna mreža"
        }
    },
    {
        "099": {
            "mjesto": "Hrvatski telekom",
            "vrsta": "Mobilna mreža"
        }
    },
    {
        "0800": {
            "mjesto": "Besplatni pozivi",
            "vrsta": "Posebne usluge"
        }
    },
    {
        "060": {
            "mjesto": "Komercijalni pozivi",
            "vrsta": "Posebne usluge"
        }
    },
    {
        "061": {
            "mjesto": "Glasovanje telefonom",
            "vrsta": "Posebne usluge"
        }
    },
    {
        "064": {
            "mjesto": "Usluge s neprimjerenim sadržajem",
            "vrsta": "Posebne usluge"
        }
    },
    {
        "065": {
            "mjesto": "Nagradne igre",
            "vrsta": "Posebne usluge"
        }
    },
    {
        "069": {
            "mjesto": "Usluge namijenjene djeci",
            "vrsta": "Posebne usluge"
        }
    },
    {
        "072": {
            "mjesto": "jedinstveni pristupni broj za cijelu državu za posebne usluge",
            "vrsta": "Posebne usluge"
        }
    }
]


# pomoćna funkcija za čišćenje broja
def ocisti_broj(broj: str):
    tocan = ""
    for i in broj:
        if i.isdigit():
            tocan += i
    if tocan.startswith("00385"):
        tocan = "0" + tocan[5:]
    elif tocan.startswith("385"):
        tocan = "0" + tocan[3:]
    return tocan


# pomoćna funkcija za pronalazak pozivnog broja
def pronadi_pozivni(tocan: str):
    svi_pozivni = []
    for zapis in pozivni_brojevi:
        for pozivni in zapis.keys():
            svi_pozivni.append(pozivni)
    for pozivni in sorted(svi_pozivni, key=len, reverse=True):
        if tocan.startswith(pozivni):
            return pozivni
    return None


# pomoćna funkcija za validaciju duljine
def provjeri_duljinu(vrsta: str, broj_ostatak: str):
    duljina = len(broj_ostatak)
    if vrsta in ["Fiksna mreža", "Mobilna mreža"]:
        return duljina in [6, 7]
    elif vrsta == "Posebne usluge":
        return duljina == 6
    return False


def validiraj_broj_telefona(broj: str):

    rjecnik = {
        "pozivni_broj": str(),
        "broj_ostatak": str(),
        "vrsta": str(),
        "mjesto": str(),
        "operator": str(),
        "validan": bool()
    }

    # čišćenje broja
    tocan = ocisti_broj(broj)

    # pronalazak pozivnog
    pronadeni_pozivni = pronadi_pozivni(tocan)
    if not pronadeni_pozivni:
        return rjecnik

    # ostatak broja
    broj_ostatak = tocan[len(pronadeni_pozivni):]

    rjecnik["pozivni_broj"] = pronadeni_pozivni
    rjecnik["broj_ostatak"] = broj_ostatak

    # podaci o broju
    podaci = None
    for zapis in pozivni_brojevi:
        if pronadeni_pozivni in zapis:
            podaci = zapis[pronadeni_pozivni]
            break
    if not podaci:
        return rjecnik

    vrsta = podaci["vrsta"]
    mjesto = podaci["mjesto"]

    # provjera duljine
    validan = provjeri_duljinu(vrsta, broj_ostatak)

    # popunjavanje rječnika
    rjecnik["vrsta"] = vrsta
    if vrsta == "Mobilna mreža":
        rjecnik["mjesto"] = None
        rjecnik["operator"] = mjesto
    elif vrsta == "Fiksna mreža":
        rjecnik["mjesto"] = mjesto
        rjecnik["operator"] = None
    elif vrsta == "Posebne usluge":
        rjecnik["mjesto"] = None
        rjecnik["operator"] = None

    rjecnik["validan"] = validan

    return rjecnik


print(validiraj_broj_telefona("091 123 4567"))

