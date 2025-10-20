broj1 = float(input("Unesi prvi broj: "))
broj2 = float(input("Unesi drugi broj: "))
operator = input("Unesi operator (+, -, *, /): ")

if operator == '+':
    rezultat = broj1 + broj2
    print(f"Rezultat operacije {broj1} + {broj2} je {rezultat}.")
elif operator == '-':
    rezultat = broj1 - broj2
    print(f"Rezultat operacije {broj1} - {broj2} je {rezultat}.")
elif operator == '*':
    rezultat = broj1 * broj2
    print(f"Rezultat operacije {broj1} * {broj2} je {rezultat}.")
elif operator == '/':
    if broj2 == 0:
        print("Dijeljenje s nulom nije dozvoljeno!")
    else:
        rezultat = broj1 / broj2
        print(f"Rezultat operacije {broj1} / {broj2} je {rezultat}.")
else:
    print("Nepodržani operator!")
