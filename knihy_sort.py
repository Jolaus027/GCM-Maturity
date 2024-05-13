"""
1. Na začiatku si vytvorime pole s náhodným počtom kníh a priradíme knihám náhodnú výšku
2. Potom knihy zoradíme
3. Nasledne vypočítame priemer kníh a medián kníh
"""

import random

knihy = []
for i in range(random.randrange(5,15)):

    knihy.append(random.randrange(1,50))

print(knihy)

#sort

for i in range(len(knihy)):

    for b in range(len(knihy)-1):

        if knihy[b] > knihy[b+1]:

            knihy[b], knihy[b+1] = knihy[b+1], knihy[b]

print(knihy)

#priemer

pocet = 0
for i in knihy:

    x = int(i)
    pocet +=x

    i = str(i)

primer = pocet//len(knihy)

print("priemer:", primer)

#median

x = 0
median = 0
if len(knihy)%2 == 0:

    x += len(knihy)//2
    m = (knihy[x]+knihy[x-1])
    median = m//2

else:

    x += len(knihy)//2

    median = knihy[x]

print("median:",median)