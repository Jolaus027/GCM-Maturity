
import tkinter

canvas = tkinter.Canvas(width=1000, height=800)
canvas.pack()

posun = 10

file = open("doc.txt", "r")
text_read = file.readline().strip()

#nekonecne, je to optional
while True:
    for i in range(len(text_read)):
    
        canvas.create_text(500, 500, text = text_read[i:i+posun], tag="text")
        canvas.after(500)
        canvas.update()
        canvas.delete("text") 

tkinter.mainloop()
