"""
Na vstupe sú dvojice celých čísel reprezentujúce súradnice bodov v rovine. V každom riadku sú dve čísla oddelené medzerou.

a) Napíšte program, ktorý načíta tieto údaje zo vstupného súboru udaje.txt (ten si najskôr musíte vytvoriť).

b) Body vykreslite.

c) Doplňte program tak, aby vypísal dĺžku strany (rovnobežnej s osou x) minimálneho obdĺžnika, ktorý obsahuje všetky zadané body
"""

import tkinter

body = []

with open("udaje.txt") as file:

    for line in file:
        body += [line.split()]
  
canvas = tkinter.Canvas(width=1000,height=1000)
canvas.pack()

for i in range(len(body)):

    canvas.create_oval((int(body[i][0])), (int(body[i][1])), ((int(body[i][0]))-10), ((int(body[i][1]))-10),fill="red")

x = [int(body[i][0]) for i in range(len(body))]
y = [int(body[i][1]) for i in range(len(body))]

canvas.create_rectangle(max(x),max(y),min(x)-10,min(y)-10)

print("Dlzka strany je", max(x)-min(x))
tkinter.mainloop()



