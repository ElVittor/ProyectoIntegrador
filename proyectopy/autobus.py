from tkinter import messagebox, Tk, Button , Frame , Entry , Label 
from controladorBD import *
controlador = controladorBD()

#Metodo que usa mi objeto controlador para insertar
def ejectutaInsert():
    controlador.guardarBus(modelo.get(), matri.get(), asientos.get(), tanque.get(), marca.get())

ventana = Tk()
ventana.title("AUTOBUS")
ventana.geometry("300x400")

fondo = Frame(ventana,bg="white")
fondo.pack(expand=True,fill='both')


label = Label(fondo,text="AUTOBUS",bg="blue",fg="white")
label.place(x=0, y=0)

mar = Label(fondo,text="Marca",bg="white",fg="black")
mar.place(x=0, y=50)
marca = Entry(width="30")
marca.place(x=100, y=50)

mod = Label(fondo,text="Modelo",bg="white",fg="black")
mod.place(x=0, y=100)
modelo = Entry(width="30")
modelo.place(x=100, y=100)

mat = Label(fondo,text="Matricula",bg="white",fg="black")
mat.place(x=0, y=150)
matri = Entry(width="30")
matri.place(x=100, y=150)

asi = Label(fondo,text="N de asientos",bg="white",fg="black")
asi.place(x=0, y=200)
asientos = Entry(width="30")
asientos.place(x=100, y=200)

tanq = Label(fondo,text="capasidad de tanque",bg="white",fg="black")
tanq.place(x=0, y=250)
tanque = Entry(width="20")
tanque.place(x=130, y=250)

btnatasigdato= Button(fondo,text="Asignar ruta",fg="black",bg="white")
btnatasigdato.place(x=100,y=300,width=100,height=30)

btnatreporte= Button(fondo,text="Guardar Datos",fg="black",bg="white", command=ejectutaInsert)
btnatreporte.place(x=100,y=340,width=100,height=30)















ventana.mainloop()
