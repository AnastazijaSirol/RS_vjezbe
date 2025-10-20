lozinka = input("Unesi lozinku: ")

def provjera_lozinke(lozinka):

    #Broj znakova
    if (len(lozinka)<7 and len(lozinka)>15):
        print("Lozinka mora sadržavati između 8 i 15 znakova!")
        return
    
    #Veliko slovo i broj
    veliko_slovo = any(slovo.isupper() for slovo in lozinka)
    broj = any(slovo.isdigit() for slovo in lozinka)
    if not (veliko_slovo and broj):
        print("Lozinka mora sadržavati barem jedno veliko slovo i jedan broj")
        return
    
    #Zabranjene riječi
    lozinka_lower = lozinka.lower()
    if "password" in lozinka_lower or "lozinka" in lozinka_lower:
        print("Lozinka ne smije sadržavati riječi 'password' ili 'lozinka'")
        return
    
    print("Lozinka je jaka!")

provjera_lozinke(lozinka)