from tkinter import messagebox, Tk, Button , Frame , Entry , Label 

ventana = Tk()
ventana.title("LOGEO")
ventana.geometry("300x250")


fondo = Frame(ventana,bg="white")
fondo.pack(expand=True,fill='both')



bustexto = Label(fondo,text="INICIO DE SECI0N",bg="blue",fg="white")
bustexto.place(x=0, y=0)








bustexto = Label(fondo,text="Usuario",bg="white",fg="black")
bustexto.place(x=0, y=50)
paradas = Entry(width="30")
paradas.place(x=100, y=50)

bustexto = Label(fondo,text="Contraseña",bg="white",fg="black")
bustexto.place(x=0, y=100)
paradas = Entry(width="30")
paradas.place(x=100, y=100)









btnatasigdato= Button(fondo,text="INICIAR SECCION",fg="black",bg="white")
btnatasigdato.place(x=100,y=150,width=100,height=50)

















ventana.mainloop()
