"""
Vo vstupnom súbore had.txt je jeden riadok zložený zo znakov H,B,P - je to zakódovaná cesta hada, kde H je hore, D je dole, P je vpravo a L je vľavo.

Načítajte túto cestu a vykreslite ju, pričom jeden „krok hada" má dĺžku 5 pixelov.
"""

import tkinter

with open("had.txt") as file:

    hadik = [i.split() for i in file]
    
canvas = tkinter.Canvas(width=1000,height=1000)
canvas.pack()

coords = [552,554,552,554]
p = 15

for i in hadik[0]:

    if i == "D":
            coords[3] += p
            canvas.create_line(coords)
            coords[1] += p
    elif i == "H": 
            coords[1] -= p
            canvas.create_line(coords)
            coords[3] -= p
    elif i == "L":
            coords[0] -= p
            canvas.create_line(coords)
            coords[2] -= p
    elif i == "P":
            coords[2] += p
            canvas.create_line(coords)
            coords[0] += p
        
    canvas.after(500)
    canvas.update()
    
canvas.mainloop()
