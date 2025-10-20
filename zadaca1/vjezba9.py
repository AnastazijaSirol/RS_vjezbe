def ukloni_duplikate(lista):
    nova_lista = []
    for broj in lista:
        if broj not in nova_lista:
            nova_lista.append(broj)
    return nova_lista

lista = [1, 2, 3, 4, 3, 2, 1, 6, 3]

print(ukloni_duplikate(lista))
