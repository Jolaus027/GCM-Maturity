#18. V štvorci je vpísaný kruh, vygenerovať väčšie množstvo bodov a vypísať, koľko z nich padlo kam

import tkinter
import random

canvas = tkinter.Canvas(width=500,height=500)
canvas.pack()


canvas.create_rectangle(50,50,450,450)
canvas.create_oval(50,50,450,450)

def is_oval(x,y):

    if (x - 250)**2 / (200**2) + ((y-250)**2) / (200**2) <= 1:
        return True
    else:
        return False

for i in range(random.randrange(20,90)):

    x = random.randrange(50,440)
    y = random.randrange(50,440)
    if is_oval(x,y):
        canvas.create_oval(x,y,x+10,y+10,fill="blue")

    else:
        canvas.create_oval(x,y,x+10,y+10,fill="red")

canvas.mainloop()
