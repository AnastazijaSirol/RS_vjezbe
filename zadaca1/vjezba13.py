#1
def prvi_i_zadnji(lista): return (lista[0], lista[-1])

lista=[1, 2, 3]

print(prvi_i_zadnji(lista))

#2
def min_i_max(lista):
    if not lista:
        return None

    najmanji = najveci = lista[0]

    for broj in lista:
        if broj < najmanji:
            najmanji = broj
        elif broj > najveci:
            najveci = broj

    return (najmanji, najveci)

print(min_i_max(lista))

#3
def presjek(skup1, skup2):
    return {element for element in skup1 if element in skup2}

lista2=[1, 2, 4, 5, 6]

print(presjek(lista, lista2))
