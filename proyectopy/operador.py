from tkinter import messagebox, Tk, Button , Frame , Entry , Label 
from controladorBD import *

controlador = controladorBD()

#Metodo que usa mi objeto controlador para insertar
def ejectutaInsert():
    controlador.guardarOperador(appEntry.get(), ammEntry.get(), num.get(), licencia.get(), vigencia.get(), nombre.get())
    
ventana = Tk()
ventana.title("OPERADOR")
ventana.geometry("300x400")


fondo = Frame(ventana,bg="white")
fondo.pack(expand=True,fill='both')

label = Label(fondo,text="OPERADOR",bg="blue",fg="white")
label.place(x=0, y=0)

nom = Label(fondo,text="Nombre",bg="white",fg="black")
nom.place(x=0, y=50)
nombre = Entry(width="30")
nombre.place(x=100, y=50)

app = Label(fondo,text="Apellido paterno",bg="white",fg="black")
app.place(x=0, y=100)
appEntry = Entry(width="30")
appEntry.place(x=100, y=100)

amm = Label(fondo,text="Apellido materno",bg="white",fg="black")
amm.place(x=0, y=150)
ammEntry = Entry(width="30")
ammEntry.place(x=100, y=150)


number = Label(fondo,text="Numero de empleado",bg="white",fg="black")
number.place(x=0, y=200)
num = Entry(width="30")
num.place(x=100, y=200)

lic = Label(fondo,text="Licencia",bg="white",fg="black")
lic.place(x=0, y=250)
licencia = Entry(width="30")
licencia.place(x=100, y=250)

vig = Label(fondo,text="vigencia",bg="white",fg="black")
vig.place(x=0, y=300)
vigencia = Entry(width="30")
vigencia.place(x=100, y=300)

btnatasigdato= Button(fondo,text="Insertar",fg="black",bg="white", command=ejectutaInsert)
btnatasigdato.place(x=180,y=340,width=80,height=50)

btnatreporte= Button(fondo,text="Eliminar",fg="black",bg="white")
btnatreporte.place(x=30,y=340,width=80,height=50)















ventana.mainloop()
