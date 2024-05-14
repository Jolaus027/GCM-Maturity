"""
19. Rozdeliť 4 cif. číslo na cifry a uložiť do premenných, 
vypísať cif. súčet čísla, koľko väčších 4-cif. čísel existuje ako zadane číslo, 
číslo premeniť na HH:MM:SS
"""
cislo = 9999
rozdel = [int(i) for i in str(cislo)]
cas = []

print("Ciferny sucet je:",sum(rozdel),"\nExistuje",9999-cislo,"vacsich 4-cifernych cisel ako cislo",cislo)

for i in range(2):
    cas.append(cislo%60)
    cislo //=60
    cas.append(cislo)
    
cas.pop(1)
print(cas[-1],":",cas[-2],":",cas[-3])