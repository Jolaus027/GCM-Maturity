#16.Prevod čísla z 2 do 10 sústavy, prevod čísla s ľubovoľnej sústavy (2-9) do 10 (iba cele čísla)

cislo = (input("Zadaj cislo v 2 sustave a potom v 8 susteve\noddeluj medzerou: ")).split()

def convert(x,cislo):

        vysled = 0
        for i in range(len(cislo)):
                vysled += int(cislo[-i-1])*(x**i)
                

        return(vysled)

# z 2 do 10 sustavy
print("Z 2 do 10>>",(convert(2,cislo[0])))
# z 8 do 10 sustavy
print("Z 8 do 10>>",(convert(8,cislo[1])))