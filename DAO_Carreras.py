import mysql.connector

class DAO_Carreras():
    def __init__(self, nombre: str):
        self._nombre = nombre
        self._listacarreras = []
        self._mydb = mysql.connector.connect(
                      host="localhost",
                      user="root",
                      password="123456",
                      database="carreras"
                  )
        self._mycursor = self._mydb.cursor()

    def añadir(self, carrera):
        sql = "INSERT INTO carreras.carreras (nombre) VALUES (%s)"
        val = [carrera.get_nombre()]
        self._mycursor.execute(sql, val)
        self._mydb.commit()

    def ver(self):
        self._mycursor.execute("SELECT * FROM carreras")
        self._myresult = self._mycursor.fetchall()
        return self._myresult
    
    def actualizar(self, carrera):
        sql = "UPDATE carreras.carreras SET nombre = %s WHERE idcarreras = %s"
        valores = (carrera.get_nombre(), carrera.get_idCarrera())
        self._mycursor.execute(sql, valores)
        self._mydb.commit()
    
    def borrar(self,carrera):
        sql = "DELETE FROM carreras.carreras WHERE idcarreras = %s"
        consulta_valor = carrera.get_idCarrera()
        self._mycursor.execute(sql,consulta_valor)
        self._mydb.commit() 
