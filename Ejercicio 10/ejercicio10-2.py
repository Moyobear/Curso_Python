from tkinter import *
master = Tk()
elemento = StringVar()
listbox = Listbox(master)
for item in ["Java", "JavaScript", "HTML", "CSS", "Python", "React", "Redux", "Django"]:
    listbox.insert(END, item)
listbox.pack()
label = Label(text="Lista de Tecnologías")
label.pack()
master.mainloop()
