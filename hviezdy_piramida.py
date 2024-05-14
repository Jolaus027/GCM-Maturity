#6. N hviezdičiek (pyramídy) 
import tkinter

canvas = tkinter.Canvas(width=500,height=500)
canvas.pack()

coords = [250,50,200,200,50,250,200,300,250,450,300,300,450,250,300,200]
for i in range(20):
    for i in range(len(coords)):

        if (i+1) % 2 == 0:
            coords[i] += 5

    canvas.create_polygon(coords,outline="red")

canvas.mainloop()

