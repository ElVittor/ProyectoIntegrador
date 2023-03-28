from tkinter import messagebox, Tk, Button , Frame , Entry , Label 
from controladorBD import *


controlador = controladorBD()

#Metodo que usa mi objeto controlador para insertar
def ejectutaInsert():
    controlador.guardarAlumno(apEntry.get(), amEntry.get(), carrera.get(),matricula.get(),ruta.get(),turno.get(),tipoViaje.get(),nombre.get())

ventana = Tk()
ventana.title("RUTA")
ventana.geometry("300x500")


fondo = Frame(ventana,bg="white")
fondo.pack(expand=True,fill='both')



label = Label(fondo,text="ALUMNO",bg="blue",fg="white")
label.place(x=0, y=0)



nombreTexto = Label(fondo,text="Nombre",bg="white",fg="black")
nombreTexto.place(x=0, y=50)
nombre = Entry(width="30")
nombre.place(x=100, y=50)

ap = Label(fondo,text="Apellido paterno",bg="white",fg="black")
ap.place(x=0, y=100)
apEntry = Entry(width="30")
apEntry.place(x=100, y=100)

am = Label(fondo,text="Apellido materno",bg="white",fg="black")
am.place(x=0, y=150)
amEntry = Entry(width="30")
amEntry.place(x=100, y=150)


carreraText= Label(fondo,text="Carrera",bg="white",fg="black")
carreraText.place(x=0, y=200)
carrera = Entry(width="30")
carrera.place(x=100, y=200)

matri = Label(fondo,text="matricula",bg="white",fg="black")
matri.place(x=0, y=250)
matricula = Entry(width="30")
matricula.place(x=100, y=250)

route = Label(fondo,text="ruta",bg="white",fg="black")
route.place(x=0, y=300)
ruta = Entry(width="30")
ruta.place(x=100, y=300)

turn = Label(fondo,text="turno",bg="white",fg="black")
turn.place(x=0, y=350)
turno = Entry(width="30")
turno.place(x=100, y=350)

typeViaje = Label(fondo,text="tipo de viaje",bg="white",fg="black")
typeViaje.place(x=0, y=400)
tipoViaje = Entry(width="30")
tipoViaje.place(x=100, y=400)


btnatasigdato= Button(fondo,text="Registrar Alumno",fg="black",bg="white", command=ejectutaInsert)
btnatasigdato.place(x=180,y=430,width=80,height=50)

btnatreporte= Button(fondo,text="Generar reporte",fg="black",bg="white")
btnatreporte.place(x=30,y=430,width=80,height=50)



ventana.mainloop()
