from tkinter import messagebox, Tk, Button , Frame , Entry , Label 

ventana = Tk()
ventana.title("RUTA")
ventana.geometry("300x450")


fondo = Frame(ventana,bg="white")
fondo.pack(expand=True,fill='both')




bustexto = Label(fondo,text="Seleccione la ruta a asignar",bg="white",fg="black")
bustexto.place(x=0, y=50)

bustexto = Label(fondo,text="Seleccione un operador",bg="white",fg="black")
bustexto.place(x=0, y=100)

bustexto = Label(fondo,text="Seleccione un autobus",bg="white",fg="black")
bustexto.place(x=0, y=150)


bustexto = Label(fondo,text="Seleccione una hora de salida",bg="white",fg="black")
bustexto.place(x=0, y=200)

bustexto = Label(fondo,text="Seleccione una hora de llegada",bg="white",fg="black")
bustexto.place(x=0, y=250)

bustexto = Label(fondo,text="total paradas",bg="white",fg="black")
bustexto.place(x=0, y=300)




btnatoreg= Button(fondo,text="Regresar",fg="black",bg="white")
btnatoreg.place(x=200,y=300,width=60,height=30)



btnatasigdato= Button(fondo,text="Asignar ruta",fg="black",bg="white")
btnatasigdato.place(x=180,y=350,width=100,height=80)

btnatreporte= Button(fondo,text="Generar reporte",fg="black",bg="white")
btnatreporte.place(x=30,y=350,width=100,height=80)


paradas = Entry(width="7")
paradas.place(x=100, y=300)











ventana.mainloop()
