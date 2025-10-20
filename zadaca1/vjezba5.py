# for petlja
broj = int(input("Unesi broj: "))
faktorijel = 1

for i in range(1, broj + 1): #drugi broj ne ulazi u raspon pa se mora dodati 1
    faktorijel *= i

print(f"Faktorijel broja {broj} je {faktorijel}")

#while petlja
broj = int(input("Unesi broj: "))
faktorijel = 1
i = 1

while i <= broj:
    faktorijel *= i
    i += 1

print(f"Faktorijel broja {broj} je {faktorijel}")
