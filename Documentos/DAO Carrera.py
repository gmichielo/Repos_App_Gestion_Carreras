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
        return self._myresult

    def actualizar(self):
        self._mycursor = self._mydb.cursor()
        sql = "UPDATE carerras.carreras SET nombre = 2 WHERE idcarrera = 1"
        self._mycursor.execute(sql)
        self._mydb.commit()
        
    def borrar(self, carrera):
        self._mycursor = self._mydb.cursor()
        sql = "DELETE FROM carerras.carreras WHERE idcarrera = %s"
        consulta_valor = carrera.get_idCarrera()
        self._mycursor.execute(sql,consulta_valor)
        self._mydb.commit()  
