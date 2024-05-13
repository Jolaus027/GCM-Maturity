#23. Input je kladné celé číslo, zisti, či je prvočíslo, ak nie, nájde nasledujúce prvočíslo smerom hore, rozloží zadane číslo na súčin prvočísel a vypíše

def prvocislo(x):

    for i in range(2,x):

        if x % i == 0:
            return False

    return True

cislo = int(input("Zadaj kladne cele cislo: "))
rozkl = []

#hladanie prvocisla
if prvocislo(cislo):

    print(f"{cislo} je to prvocislo")

else:

    rozkl.append(cislo)
    while prvocislo(cislo) == False:

        cislo+=1

    print(f"Tvoje cislo nie je prvocislo ale najblizsie smerom hore je {cislo}")

    #rozklad

    while rozkl[0] > 1:

        for i in range(2,1000):

            if rozkl[0] % i == 0:
                rozkl[0] //= i
                rozkl.append(i)

    print(f"Toto je prvociselny rozklad povodne zadaneho cisla\n{rozkl}")