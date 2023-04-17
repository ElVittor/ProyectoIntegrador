from tkinter import *
from tkinter import ttk
import tkinter as tk
from controladorBD import *

controlador = controladorBD()

def Execute_Delete_Bus():
    RSDelete=messagebox.askyesno("Confirmación de Accion: Eliminar",message=f"Desea eliminar el Autobus\nID: {varID.get()}")
    if(RSDelete==True):
        controlador.DeleteBus(varID.get())

def ejecutaactualizarusuario():
    RespYesNo=messagebox.askyesno("Actualizar",message=f"Desea actualizar el siguiente usuario: \nID: {varID.get()}\nMarca: {varmarca.get()}\nModelo: {varmodelo.get()}\nMatricula: {varmatricula.get()}\nNumero de Asientos: {varasientos.get()}\nCapacidad del Tanque: {varcaptanq.get()}")
    if RespYesNo==True:
        controlador.editBus(varID.get(),varmodelo.get(),varmatricula.get(),varasientos.get(),varcaptanq.get(),varmarca.get())

def ejecutaactalizaroperador():
    RespYesNo=messagebox.askyesno("Actualizar",message=f"Desea actualizar el siguiente Operador: \nID: {varIDO.get()}\nNombre: {varnombre.get()}\nApellido Paterno: {varap.get()}\nApellido Materno: {varam.get()}\nNumero de empleado: {varNumEmpleado.get()}\nLicencia: {varlicenica.get()}\nVigencia: {varvigencia.get()}")
    if RespYesNo==True:
        controlador.editOper(varIDO.get(),varap.get(),varam.get(),varNumEmpleado.get(),varlicenica.get(),varvigencia.get(),varnombre.get())

def ejecutaeliminaroperador():
    RSDelete=messagebox.askyesno("Confirmación de Accion: Eliminar",message=f"Desea eliminar el Operador\nID: {varIDEO.get()}")
    if(RSDelete==True):
        controlador.DeleteBus(varIDEO.get())
        
ventana=Tk()
ventana.title("CRUD de Edicion y Eliminacion de Autobuses")
ventana.geometry("500x300")
#paso 2
panel=ttk.Notebook(ventana) #crea un panel para usar dentro de la ventana, con .pack lo vamos a ubicar dentro de la ventana
panel.pack(fill="both",expand="yes")

pestaña4=ttk.Frame(panel)#pestaña 4 va al panel
pestaña5=ttk.Frame(panel)
pestaña6=ttk.Frame(panel)
pestaña7=ttk.Frame(panel)

titulo = Label(pestaña4, text='Editar Autobuses', fg = 'purple', font=('Modern', 18)).pack()
#editBus(id,modelo,matricula,NoAsientos,capacidadTanque,marca):

varID=tk.StringVar()#para vaciar el Entry
lblID=Label(pestaña4,text="ID Autbus a Editar: ").pack()
txtID=Entry(pestaña4,textvariable=varID).pack() #text variable te pide la variable donde va aguardar

varmodelo=tk.StringVar()#para vaciar el Entry
lblmodelo=Label(pestaña4,text="Modelo: ").pack()
txtmodelo=Entry(pestaña4,textvariable=varmodelo).pack() #text variable te pide la variable donde va aguardar

varmatricula=tk.StringVar()#para vaciar el Entry
lblCor2=Label(pestaña4,text="Matricula: ").pack()
txtCor2=Entry(pestaña4,textvariable=varmatricula).pack() #text variable te pide la variable donde va aguardar

varasientos=tk.StringVar()#para vaciar el Entry
lblCon2=Label(pestaña4,text="Numero de Asientos: ").pack()
txtCon2=Entry(pestaña4,textvariable=varasientos).pack() #text variable te pide la variable donde va aguardar

varcaptanq=tk.StringVar()#para vaciar el Entry
lbltan=Label(pestaña4,text="Capacidad del tanque de combustible: ").pack()
txttan=Entry(pestaña4,textvariable=varcaptanq).pack()

varmarca=tk.StringVar()#para vaciar el Entry
lblNom2=Label(pestaña4,text="Marca: ").pack()
txtNom2=Entry(pestaña4,textvariable=varmarca).pack()

btnEditar=Button(pestaña4,text="Editar Usuario",command=ejecutaactualizarusuario).pack()#Usamos el ejecutar insert para guardar la información

#Eliminar
varID=tk.StringVar()#para vaciar el Entry
titulo=Label(pestaña5,text="Eliminar Usuario",fg="blue",font=("Modern",18)).pack() #posicionamos un titulo en una etiqueta, en pestaña 1, con texto, color de letra, tipo de fuente y tamaño, colocandolo con el pack
lbID2=Label(pestaña5,text="ID del Usuario a Eliminar: ").pack()
txtID2=Entry(pestaña5,textvariable=varID).pack()
btnEliminar=Button(pestaña5,text="Eliminar Usuario",command=Execute_Delete_Bus).pack()#Usamos el ejecutar insert para guardar la información

#Editar eliminar operador

titulo = Label(pestaña6, text='Editar Operador', fg = 'purple', font=('Modern', 18)).pack()
#editBus(id,modelo,matricula,NoAsientos,capacidadTanque,marca):

varIDO=tk.StringVar()#para vaciar el Entry
lblIDO=Label(pestaña6,text="ID Operador a Editar: ").pack()
txtID==Entry(pestaña6,textvariable=varIDO).pack() #text variable te pide la variable donde va aguardar

varnombre=tk.StringVar()#para vaciar el Entry
lblmodeloO=Label(pestaña6,text="Nombre: ").pack()
txtmodeloO=Entry(pestaña6,textvariable=varnombre).pack() #text variable te pide la variable donde va aguardar

varap=tk.StringVar()#para vaciar el Entry
lblCor2O=Label(pestaña6,text="Apellido Paterno: ").pack()
txtCor2O=Entry(pestaña6,textvariable=varap).pack() #text variable te pide la variable donde va aguardar

varam=tk.StringVar()#para vaciar el Entry
lblCon2O=Label(pestaña6,text="Apellido Materno: ").pack()
txtCon2O=Entry(pestaña6,textvariable=varam).pack() #text variable te pide la variable donde va aguardar

varNumEmpleado=tk.StringVar()#para vaciar el Entry
lbltanO=Label(pestaña6,text="Número de empleado: ").pack()
txttanO=Entry(pestaña6,textvariable=varNumEmpleado).pack()

varlicenica=tk.StringVar()#para vaciar el Entry
lblNom2O=Label(pestaña6,text="Licencia: ").pack()
txtNom2O=Entry(pestaña6,textvariable=varlicenica).pack()

varvigencia=tk.StringVar()#para vaciar el Entry
lblNom2O=Label(pestaña6,text="Vigencia: ").pack()
txtNom2O=Entry(pestaña6,textvariable=varvigencia).pack()

btnEditarO=Button(pestaña6,text="Editar Usuario",command=ejecutaactalizaroperador).pack()#Usamos el ejecutar insert para guardar la información

#Eliminar
varIDEO=tk.StringVar()#para vaciar el Entry
tituloEO=Label(pestaña7,text="Eliminar Operador",fg="blue",font=("Modern",18)).pack() #posicionamos un titulo en una etiqueta, en pestaña 1, con texto, color de letra, tipo de fuente y tamaño, colocandolo con el pack
lbID2EO=Label(pestaña7,text="ID del Operador a Eliminar: ").pack()
txtID2EO=Entry(pestaña7,textvariable=varIDEO).pack()
btnEliminarEO=Button(pestaña7,text="Eliminar Operador",command=ejecutaeliminaroperador).pack()

panel.add(pestaña4, text='Editar usuarios')
panel.add(pestaña5, text='Eliminar usuarios')
panel.add(pestaña6, text='Editar Operador')
panel.add(pestaña7, text='Eliminar Operador')

ventana.mainloop()