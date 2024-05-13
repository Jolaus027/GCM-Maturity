#ZAUJIMAVO NAPROGRAMOVANE
slovo = "TySiGay"

for i in range((len(slovo))*2):

    if i > len(slovo):
        print(slovo[:((len(slovo))-i)])

    else:
        print(slovo[:i])