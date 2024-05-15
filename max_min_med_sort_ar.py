#8. Postupnosti (sort, med, max, min, aritm. priemer)
postupnost = (input("Postupnost, oddel medzerou: ")).split()

def buble(sort):

    for i in range(len(sort)):
        for k in range(len(sort)-1):
            
            if int(sort[i]) < int(sort[k]):
                sort[i], sort[k] = sort[k], sort[i]

    return sort

def med(sort):

    if len(sort) % 2 == 0:
        return (int(sort[len(sort)//2]) + int(sort[(len(sort)//2)+1])) / 2

    else:
        return int(sort[(len(sort)//2)])

def priemer(p):
    
    priemer = 0

    for i in p:
        priemer += int(i)

    return round((priemer/len(p)),2)

print("Postupnost:",postupnost)
print("Sort:",buble(postupnost))
print("Median:",med(buble(postupnost)))
print("Priemer:",priemer(postupnost))
print("Max:",buble(postupnost)[-1])
print("Min:",buble(postupnost)[0])