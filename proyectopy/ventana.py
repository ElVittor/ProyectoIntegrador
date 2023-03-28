from tkinter import messagebox, Tk, Button , Frame , Entry , Label

  


ventana = Tk()
ventana.title("BIENVENIDO")
ventana.geometry("300x300")


fondo = Frame(ventana,bg="white")
fondo.pack(expand=True,fill='both')



#botones

btnregistrarruta= Button(fondo,text="Ruta",fg="black",bg="white")
btnregistrarruta.place(x=20,y=40,width=100,height=80)


btnalumno= Button(fondo,text="Autobus",fg="black",bg="white")
btnalumno.place(x=170,y=40,width=100,height=80)

btnconducto= Button(fondo,text="Alumnos",fg="black",bg="white")
btnconducto.place(x=20,y=200,width=100,height=80)

btnatobus= Button(fondo,text="Operadores",fg="black",bg="white")
btnatobus.place(x=170,y=200,width=100,height=80)




#textos
bustexto = Label(fondo,text="Gestion de pollobus",bg="white",fg="black")
bustexto.place(x=100, y=0)

mostrar = Label(fondo,text="Registrar:",bg="white",fg="black")
mostrar.place(x=10, y=520)

registrar = Label(fondo,text="Mostrar:",bg="white",fg="black")
registrar.place(x=10, y=570)




ventana.mainloop()
