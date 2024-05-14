#4. Postupnosť 30 čísel (kladné, záporné, nulové, 3 maxy, 3 miny + indexy, sort)

import random

postup = [random.randint(-100,100) for i in range(30)]
povodne = postup[:]
index = 0
zero = 0

for i in range(len(postup)):
    for x in range(len(postup)-1):

        if postup[x] > postup[i]:
            postup[i], postup[x] = postup[x], postup[i]

for i in range(len(postup)):
    if postup[i] < 0:
        index += 1
    elif postup[i] == 0:
        zero = 1

print("Povodne:",povodne)
print("Sort:",postup)

print("Zaporne:",postup[:index])
print("Kladne:",postup[index+zero:])

max_min_i = [povodne.index(i) for i in postup[-3:]]
print("3 max:",postup[-3:],"pociatocny index:",max_min_i)
max_min_i = [povodne.index(i) for i in postup[:3]]
print("3 min:",postup[:3],"pociatocny index:",max_min_i)

if 0 in povodne:
    print("V postupnosti je nula na pozicii",povodne.index(0))