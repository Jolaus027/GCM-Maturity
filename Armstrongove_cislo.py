"""
Celé číslo 153 sa nazýva Armstrongovo číslo pre svoju zaujímavú vlastnosť: 
153-13 + 53 +33 t.j. súčet tretích mocnín cifier sa rovná samotnému číslu. 
Zostavte program, ktorým nájdete všetky trojciferné Armstrongove čísla.
"""
arm = []

for i in range(100,1000):

    x = (int((str(i))[0])**3) + (int((str(i))[1])**3) + (int((str(i))[2])**3)
    if x == i:
        arm.append(i)
print(arm)