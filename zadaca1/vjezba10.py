def brjoanje_rijeci(tekst):
    tekst = tekst.lower()
    
    for znak in [".", ",", "!", "?", ":", ";"]:
        tekst = tekst.replace(znak, "")
    
    rijeci = tekst.split()
    
    brojac = {}
    
    for rijec in rijeci:
        if rijec in brojac:
            brojac[rijec] += 1
        else:
            brojac[rijec] = 1
    
    return brojac

text="Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."

print(brjoanje_rijeci(text))
