#13. Slovo print do canvasu, písmená náhodnej farby, otočenie v smere hodinových ručičieka
import tkinter
import random

canvas=tkinter.Canvas(width=500,height=300)
canvas.pack()

colors = ["black", "red", "green", "blue", "yellow",
    "cyan", "magenta", "orange", "purple", "pink", "brown",
    "darkgray"]

slovo = "SLOVO"
diff = 0

for i in slovo:

    diff += 25
    color = random.choice(colors)
    canvas.create_text(30+diff,100,text=i,font=('Arial', 24),fill=color)
    colors.remove(color)

diff = 0
for i in slovo[::-1]:
    
    diff += 30
    canvas.create_text(30+diff,150,text=i,font=('Arial', 24),fill=random.choice(colors),angle=90)

tkinter.mainloop()
