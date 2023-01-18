from tkinter import *


def seleccionar():
    monitor.config(text="{}".format(opcion.get()))


def reset():
    opcion.set(None)
    monitor.config(text="")


root = Tk()
opcion = StringVar()
# sin opción seleccionada:
opcion.set(None)
Radiobutton(root, text="JavaScript", variable=opcion,
            value='JavaScript', command=seleccionar).pack(anchor=W)

Radiobutton(root, text="Python", variable=opcion,
            value='Python', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="React", variable=opcion,
            value='React', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Redux", variable=opcion,
            value='Redux', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="Java", variable=opcion,
            value='Java', command=seleccionar).pack(anchor=W)
Radiobutton(root, text="HTML y CSS", variable=opcion,
            value='HTML y CSS', command=seleccionar).pack(anchor=W)

monitor = Label(root)
monitor.pack()
Button(root, text="Reset", command=reset).pack()

root.mainloop()
