from tkinter import messagebox
import sqlite3
import bcrypt


class controladorBD:
    def __init__(self):
        pass
    
    def conexionBD(self):
        try:
            conexion = sqlite3.connect(r'C:\Users\Edgar\OneDrive\Documentos\GitHub\ProyectoIntegrador\proyectopy\pollobusBD.db')
            
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