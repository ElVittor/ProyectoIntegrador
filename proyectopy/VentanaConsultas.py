from tkinter import *
from tkinter import ttk
import tkinter as tk
from controladorBD import *

controlador = controladorBD()

def consulBus():
    consultarBus = controlador.consultaBus()
    tree.delete(*tree.get_children())
    for fila in consultarBus:
        tree.insert('',tk.END, values=fila)
        
def consulAlumno():
    consultarAlumno = controlador.consultaAlumno()
    tree1.delete(*tree1.get_children())
    for fila in consultarAlumno:
        tree1.insert('',tk.END, values=fila)

def consulOperador():
    consultarOperador = controlador.consultaOperador()
    tree2.delete(*tree2.get_children())
    for fila in consultarOperador:
        tree2.insert('',tk.END, values=fila)


ventana = Tk()
ventana.title('CRUD de usuarios')
ventana.geometry('500x300')

panel= ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

pestana1= ttk.Frame(panel)
pestana2= ttk.Frame(panel)
pestana3= ttk.Frame(panel)

titulo1 = Label(pestana1, text='Consultar Alumnos', fg = 'purple', font=('Modern', 18)).pack()
tree1 = ttk.Treeview(pestana1, column=("c1", "c2", "c3", 'c4', 'c5','c6', 'c7', 'c8','c9'), show='headings')

tree1.column("#1", anchor=tk.CENTER)
tree1.heading("#1", text="ID")

tree1.column("#2", anchor=tk.CENTER)
tree1.heading("#2", text="Nombre")

tree1.column("#3", anchor=tk.CENTER)
tree1.heading("#3", text="Apellido P")

tree1.column("#4", anchor=tk.CENTER)
tree1.heading("#4", text="Apellido M")

tree1.column("#5", anchor=tk.CENTER)
tree1.heading("#5", text="Carrera")

tree1.column("#6", anchor=tk.CENTER)
tree1.heading("#6", text="Matricula")

tree1.column("#7", anchor=tk.CENTER)
tree1.heading("#7", text="Ruta")

tree1.column("#8", anchor=tk.CENTER)
tree1.heading("#8", text="Turno")

tree1.column("#9", anchor=tk.CENTER)
tree1.heading("#9", text="Viaje")


tree1.pack()

btnAlumn = Button(pestana1,text='Consultar', command=consulAlumno).pack()

titulo2 = Label(pestana2, text='Consultar Autobus', fg = 'purple', font=('Modern', 18)).pack()
tree2 = ttk.Treeview(pestana2, column=("c1", "c2", "c3", 'c4', 'c5','c6','c7'), show='headings')

tree2.column("#1", anchor=tk.CENTER)
tree2.heading("#1", text="ID")

tree2.column("#2", anchor=tk.CENTER)
tree2.heading("#2", text="Apellido P")

tree2.column("#3", anchor=tk.CENTER)
tree2.heading("#3", text="Apellido M")

tree2.column("#4", anchor=tk.CENTER)
tree2.heading("#4", text="# Empleado")

tree2.column("#5", anchor=tk.CENTER)
tree2.heading("#5", text="Licencia")

tree2.column("#6", anchor=tk.CENTER)
tree2.heading("#6", text="Vigencia")

tree2.column("#7", anchor=tk.CENTER)
tree2.heading("#7", text="Nombre")
tree2.pack()

btnOperador= Button(pestana2,text='Consultar', command=consulOperador).pack()

titulo = Label(pestana3, text='Consultar Autobus', fg = 'purple', font=('Modern', 18)).pack()
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

btnConsul= Button(pestana3,text='Consultar', command=consulBus).pack()

panel.add(pestana1, text='Consultar alumnos')
panel.add(pestana2, text='Consultar operador')
panel.add(pestana3, text='Consultar autobus')

ventana.mainloop()