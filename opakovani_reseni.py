#1
#TODO

#2
cislo = 1
while cislo < 20:
    if cislo % 2 == 0:
        print(cislo)
    cislo += 1

#3
cisla = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
soucetCisel = sum(cisla)
pocetCisel = len(cisla)
prumer = soucetCisel / pocetCisel

print(f"Aritmetický průměr: {prumer}")

#4
nejakyString = "Hello World"

for pismeno in nejakyString:
    print(pismeno)