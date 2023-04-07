from tkinter import *
from tkinter import ttk
import tkinter as tk
from controladorBD import *

controlador = controladorBD()

def ejecutarConsul():
    rsConsul = controlador.consultaBus()
    tree.delete(*tree.get_children())
    for fila in rsConsul:
        tree.insert('',tk.END, values=fila)


ventana = Tk()
ventana.title('CRUD de usuarios')
ventana.geometry('500x300')

panel= ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

pestana3= ttk.Frame(panel)

titulo = Label(pestana3, text='Consultar Usuarios', fg = 'purple', font=('Modern', 18)).pack()
tree = ttk.Treeview(pestana3, column=("c1", "c2", "c3", 'c4', 'c5','c6'), show='headings')

tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="ID")

tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="Modelo")

tree.column("#3", anchor=tk.CENTER)
tree.heading("#3", text="Matricula")

tree.column("#4", anchor=tk.CENTER)
tree.heading("#4", text="Asientos")

tree.column("#5", anchor=tk.CENTER)
tree.heading("#5", text="Capacidad")

tree.column("#6", anchor=tk.CENTER)
tree.heading("#6", text="Marca")
tree.pack()
btnConsul= Button(pestana3,text='Consultar', command=ejecutarConsul).pack()

panel.add(pestana3, text='Consultar usuarios')

ventana.mainloop()