def grupiraj_po_partitetu(lista):
    rezultat = {
        "parni": [],
        "neparni": []
    }

    for broj in lista:
        if broj % 2 == 0:
            rezultat["parni"].append(broj)
        else:
            rezultat["neparni"].append(broj)
    
    return rezultat

lista=[1, 2, 3, 4, 5]

print(grupiraj_po_partitetu(lista))
