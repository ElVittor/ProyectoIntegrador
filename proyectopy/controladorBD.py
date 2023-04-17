from tkinter import messagebox
import sqlite3
import bcrypt


class controladorBD:
    def __init__(self):
        pass
    
    def conexionBD(self):
        try:
            conexion = sqlite3.connect(r'C:/Users/leon_/Documents/UPQ/5° Cuatri/PROGRMACIÓN OO/ProyectoIntegrador/proyectopy/pollobusBD.db.sql')
            
            return conexion
        except sqlite3.OperationalError:
            print('No se puede conectar')
            
            
    def guardarAlumno(self, ap, am, carrera, matri, ruta, turno, viaje, nombre):
        #1. Mandar llamar una conexion
        conx=self.conexionBD()
        
        #2. Validar vacios
        if (nombre == '' or ap == '' or am == '' or carrera == '' or matri == '' or ruta == '' or turno == '' or viaje == ''):
            messagebox.showwarning('Aguas!!', 'Formulario incompleto')
            conx.close()
        else:
            #3. Realizar el insert a la BD
            #4. Preparamos las variables necesarias
            cursor= conx.cursor()
            datos=(ap,am,carrera,matri,ruta,turno,viaje,nombre)
            sqlInsert=' insert into alumno(apellidoP,apellidoM,carrera,matricula,ruta,turno,tipoViaje,nombre) values(?,?,?,?,?,?,?,?)'
            
            #5. Ejecutamos el insert
            cursor.execute(sqlInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito", 'Usuario guardado')
        
    def guardarOperador(self,ap,am,numEmp,licencia,vigencia,nombre):
        #1. Mandar llamar una conexion
        conx=self.conexionBD()
        
        #2. Validar vacios
        if (nombre == '' or ap == '' or am == '' or numEmp == '' or licencia == '' or vigencia == ''):
            messagebox.showwarning('Aguas!!', 'Formulario incompleto')
            conx.close()
        else:
            #3. Realizar el insert a la BD
            #4. Preparamos las variables necesarias
            cursor= conx.cursor()
            datos=(ap,am,numEmp,licencia,vigencia,nombre)
            sqlInsert=' insert into operador(apellidoP, apellidoM,NumEmpleado, licencia,vigencia,nombre) values(?,?,?,?,?,?)'
            
            #5. Ejecutamos el insert
            cursor.execute(sqlInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito", 'Usuario guardado')
            
    def guardarBus(self, modelo, matricula, asientos, capacidadTanque,marca):
        #1. Mandar llamar una conexion
        conx=self.conexionBD()
        
        #2. Validar vacios
        if (marca == '' or modelo == '' or matricula == '' or asientos == '' or capacidadTanque == ''):
            messagebox.showwarning('Aguas!!', 'Formulario incompleto')
            conx.close()
        else:
            #3. Realizar el insert a la BD
            #4. Preparamos las variables necesarias
            cursor= conx.cursor()
            datos=(modelo,matricula,asientos,capacidadTanque, marca)
            sqlInsert=' insert into autobus(modelo, matricula, NumAsientos,capacidadTanque, marca) values(?,?,?,?,?)'
            
            #5. Ejecutamos el insert
            cursor.execute(sqlInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito", 'Datos guardados')
            
    def encriptarContra(self,con):
        
        #Preparamos la contraseña y la sal para hash
        conPlana = con
        conPlana = conPlana.encode() #convierte el string a bytes
        sal = bcrypt.gensalt()
        
        #Encriptamos
        conHa = bcrypt.hashpw(conPlana, sal)
        print(conHa)
        
        #Regresamos la contraseña encriptada
        return conHa
    
    def consultaBus(self):
        conx = self.conexionBD()
        try:
            cursor= conx.cursor()
            sqlSelect = 'SELECT * FROM autobus'
            cursor.execute(sqlSelect)
            RSconsul= cursor.fetchall()
            conx.close()
            return RSconsul
        except sqlite3.OperationalError:
            print('Error de consulta')
            conx.close()
            
    def consultaAlumno(self):
        conx = self.conexionBD()
        try:
            cursor= conx.cursor()
            sqlSelect = 'SELECT * FROM alumno'
            cursor.execute(sqlSelect)
            RSconsul= cursor.fetchall()
            conx.close()
            return RSconsul
        except sqlite3.OperationalError:
            print('Error de consulta')
            conx.close()
            
    def consultaOperador(self):
        conx = self.conexionBD()
        try:
            cursor= conx.cursor()
            sqlSelect = 'SELECT * FROM operador'
            cursor.execute(sqlSelect)
            RSconsul= cursor.fetchall()
            conx.close()
            return RSconsul
        except sqlite3.OperationalError:
            print('Error de consulta')
            conx.close()
            
    def consultaRuta(self):
        conx = self.conexionBD()
        try:
            cursor= conx.cursor()
            sqlSelect = 'SELECT * FROM ruta'
            cursor.execute(sqlSelect)
            RSconsul= cursor.fetchall()
            conx.close()
            return RSconsul
        except sqlite3.OperationalError:
            print('Error de consulta')
            conx.close()
            
    def editBus(self,id,modelo,matricula,NoAsientos,capacidadTanque,marca):
        #1 realizar conxión, y establecer cursor y accion
        conx=self.conexionBD() #Para acceder a la funcion conexion
        cursor=conx.cursor()
        sqlEdit="update autobus set modelo=?,matricula=?,NumAsientos=?,capacidadTanque=?,marca=? where id_autobus=?"
        if(modelo=="" or matricula=="" or NoAsientos=="" or id=="" or capacidadTanque=="" or marca==""):
            messagebox.showwarning("Cuidado","Formulario incompleto")
            conx.close()#cierra la conexion evita errores, siempre que se abre, se vuelve a cerrar despues de usar
        else:#Ahora si realizamos el inser a la base de datos
            try:
                #crear una lista para evitar errores de sintxis con los para metros que insertaremos
                datosAutobus=(modelo,matricula,NoAsientos,capacidadTanque,marca,id)#Usamos el conh para guaradar la contraseña encriptada
                #creamos la sintaxis sql para hacer el insert(lenguaje de sql).
                #5 ejecutar insert
                cursor.execute(sqlEdit,datosAutobus)#le pedimos al cursor ejecutar el insert con los datos guardados en la variable datos(antes definida)
                conx.commit()#Esta funcion se usa para guardar la informacion en la base datos, la informacion proporcionadapor el cursor
                conx.close
                messagebox.showinfo("Exito","Usuario guardado")
            except sqlite3.OperationalError:
                print("Error de Actualizacion")
                messagebox.showwarning("Cuidado","Error de Actualizacion")
            
    
    def DeleteBus(self,id):
        pass
        conx=self.conexionBD() #Para acceder a la funcion conexion
        cursor=conx.cursor()
        sqldelete="DELETE FROM autobus WHERE id_autobus=?"
        
        if(id==""):
                messagebox.showwarning("Cuidado","Escribe un Identificdor")
                conx.close()
        else:
                #3 ejecutar la consulta
            try:
                    #4Preparamos lo necesario
                cursor.execute(sqldelete,id)#Ejecuta sqlSelecct
                conx.commit()
                conx.close()
                messagebox.showinfo("Correcto","Usuario Eliminado")
            except sqlite3.OperationalError:
                print("Error de Consulta")
                
    #-------
    def editOper(self,ap,am,numEmp,licencia,vigencia,nombre):
        #1 realizar conxión, y establecer cursor y accion
        conx=self.conexionBD() #Para acceder a la funcion conexion
        cursor=conx.cursor()
        sqlEdit="update operador set nombre=?,apellidoP=?,apellidoM=?,NumEmpleado=?,licencia=?, vigencia=? where id_operador=?"
        if (nombre == '' or ap == '' or am == '' or numEmp == '' or licencia == '' or vigencia == ''):
            messagebox.showwarning('Aguas!!', 'Formulario incompleto')
            conx.close()
        else:
            #3. Realizar el insert a la BD
            #4. Preparamos las variables necesarias
            cursor= conx.cursor()
            datos=(ap,am,numEmp,licencia,vigencia,nombre)
            sqlInsert=' insert into operador(apellidoP, apellidoM,NumEmpleado, licencia,vigencia,nombre) values(?,?,?,?,?,?)'
            
            #5. Ejecutamos el insert
            cursor.execute(sqlInsert, datos)
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito", 'Usuario guardado')
        else:#Ahora si realizamos el inser a la base de datos
            try:
                #crear una lista para evitar errores de sintxis con los para metros que insertaremos
                datosOperador=(nombre,ap,am,numEmp,licencia,vigencia)#Usamos el conh para guaradar la contraseña encriptada
                #creamos la sintaxis sql para hacer el insert(lenguaje de sql).
                #5 ejecutar insert
                cursor.execute(sqlEdit,datosOperador)#le pedimos al cursor ejecutar el insert con los datos guardados en la variable datos(antes definida)
                conx.commit()#Esta funcion se usa para guardar la informacion en la base datos, la informacion proporcionadapor el cursor
                conx.close
                messagebox.showinfo("Exito","Usuario guardado")
            except sqlite3.OperationalError:
                print("Error de Actualizacion")
                messagebox.showwarning("Cuidado","Error de Actualizacion")
            
    
    def DeleteOper(self,id):
        pass
        conx=self.conexionBD() #Para acceder a la funcion conexion
        cursor=conx.cursor()
        sqldelete="DELETE FROM autobus WHERE id_autobus=?"
        
        if(id==""):
                messagebox.showwarning("Cuidado","Escribe un Identificdor")
                conx.close()
        else:
                #3 ejecutar la consulta
            try:
                    #4Preparamos lo necesario
                cursor.execute(sqldelete,id)#Ejecuta sqlSelecct
                conx.commit()
                conx.close()
                messagebox.showinfo("Correcto","Usuario Eliminado")
            except sqlite3.OperationalError:
                print("Error de Consulta")