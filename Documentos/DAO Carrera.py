import mysql.connector
class DAOcarrera:
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._mydb = mysql.connector.connect(
                      host="localhost",
                      user="root",
                      password="123456",
                      database="carreras"
                  )
        self._mycursor = self._mydb.cursor()

    def añadir(self,nombre: str):
        sql = "INSERT INTO carreras.carreras (nombre) VALUES (%s)"
        val = nombre
        self._mycursor.execute(sql, val)
        self._mydb.commit()
        #print(mycursor.rowcount, "record inserted.")      

    def ver(self):
        self._mycursor.execute("SELECT * FROM carreras")
        self._myresult = self._mycursor.fetchall()
        for row in self._myresult:
            print(row)
""""


    def actualizar(self,nombre: str, N_nombre: str):
        self._nombre = nombre



    def set_provincia(self,id: int):
        self._id = id
    def __str__(self):
        return f"Nombre: {self._nombre} idCarrera: {self._idCarrera}"
    

    mycursor = mydb.cursor()



#Mostrar tabla
mycursor.execute("SELECT * FROM alumnos")
myresult = mycursor.fetchall()
for row in myresult:
    print(row)

#Cambio de la columna despues del set con lo que coincida con la columna del WHERE
mycursor = mydb.cursor()
sql = "UPDATE universidad.alumnos SET nombre = 2 WHERE idAlumno = 1"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

#BORRAR !!!
mycursor = mydb.cursor()
consulta_sql = f"DELETE FROM alumnos WHERE nombre = 'Juanito'"
mycursor.execute(consulta_sql)
mydb.commit()
print(f"Filas afectadas: {mycursor.rowcount}")
"""