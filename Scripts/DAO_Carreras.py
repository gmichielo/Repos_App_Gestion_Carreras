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

    def añadir(self,carrera):
        sql = "INSERT INTO carreras.carreras (nombre) VALUES (%s)"
        val = [carrera.get_nombre()]
        self._mycursor.execute(sql, val)
        self._mydb.commit()

    def ver(self):
        self._mycursor.execute("SELECT * FROM carreras")
        self._myresult = self._mycursor.fetchall()
        return self._myresult