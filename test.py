from tkinter import *
from tkinter import ttk

root = Tk()
root.title ('iMedic')
canvas = Canvas(root, width = 1600, height = 800)


panewindow = ttk.Panedwindow(canvas, orient = VERTICAL)
panewindow.pack(fill = BOTH, expand = True)
paitents_frame = ttk.Frame(panewindow, width = 1600, height = 400, relief = RAISED)
prescription_frame = ttk.Frame(panewindow, width = 1600, height = 300, relief = RAISED)
panewindow.add(paitents_frame, weight = 1)
panewindow.add(prescription_frame, weight = 1)

canvas.grid(row = 0, column = 0)
photo = PhotoImage(file = './13314.png')
canvas.create_image(55, 55, image=photo)
canvas.create_text(600, 155, text = 'Welcome', font = ('Helvetica', 72, 'bold'), justify = 'center', fill='blue')
canvas.update()

root.mainloop()