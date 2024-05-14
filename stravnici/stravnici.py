"""
27. Z txt súboru načítať objednávky stravníkov, 
v každom riadku je najskôr kód stravníka, obj. jedlo označenou farbou, 
na vyber sú 4 jedla rôznymi farbami, 
vypísať najviac obj. jedlo, zistiť, či je jedlo, kt. si neobjednal nikto
"""

jedla = ["cervena","modra","zelena","fialova"]
pocet = [0 for i in range(4)]
objednavky = []

with open("udaje.txt") as file:

    for line in file:
        objednavky += [line.split()]

print(objednavky)

for i in range(len(objednavky)):

    pocet[jedla.index(objednavky[i][1])] += 1

print("Najviac objednavane jedlo je", jedla[pocet.index(max(pocet))])

if 0 in pocet:
    print("Nikto si neobjednal", jedla[pocet.index(0)])