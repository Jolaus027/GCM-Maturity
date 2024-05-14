#5. V txt súbore je zakódovaná mapa (more a súš = 0, 1), print do canvasu, vypísať akú rozlohu má more a akú súš
import tkinter

canvas = tkinter.Canvas(height=500,width=500)
canvas.pack()

udaje = []

with open("mapa.txt") as file:
    for line in file:
        udaje+=[line.split()]     
x = len(udaje[0])
y = len(udaje)

rozloha_more = 0
rozloha_sus = 0
print(x,y)

for i in range(y):

    for z in range(x):

        
        if udaje[i][z] == "0":
            canvas.create_rectangle((((500/x)*(z+1)-(500/x)),((500/y)*(i+1)-(500/y)),((500/x)*(z+1)),((500/y)*(i+1))),fill="blue")
            rozloha_more += (500/x)*(500/y)

        else:
            canvas.create_rectangle((((500/x)*(z+1)-(500/x)),((500/y)*(i+1)-(500/y)),((500/x)*(z+1)),((500/y)*(i+1))),fill="green")
            rozloha_sus += (500/x)*(500/y)
print(f"Rozloha mora: {round(rozloha_more,2)} pixelov\nRozloha suse: {round(rozloha_sus,2)} pixelov")

canvas.mainloop()
