import mysql.connector

class DAO_Carreras():
    def __init__(self, user_input: str, password_input: str):
        self.__listacarreras = []

        self.__host = "localhost"
        self.__user = user_input
        self.__password = password_input
        self.__database = "carreras_edgar&gabriel"

        self.__mydb = mysql.connector.connect(
                      host = self.__host,
                      user = self.__user,
                      password = self.__password,
                      database = self.__database
                  )
        
        self.__mycursor = self.__mydb.cursor()

    def existecia(self):
        return "Conexion Hecha"

    def añadir(self, carrera):
        sql = "INSERT INTO `carreras_edgar&gabriel`.carreras (nombre) VALUES (%s)"
        val = [carrera.get_nombre()]
        self.__mycursor.execute(sql, val)
        self.__mydb.commit()

    def ver(self):
        self.__mycursor.execute("SELECT * FROM carreras")
        self._myresult = self.__mycursor.fetchall()
        return self._myresult
    
    def actualizar(self, carrera):
        sql = "UPDATE `carreras_edgar&gabriel`.carreras SET nombre = %s WHERE idcarreras = %s"
        valores = (carrera.get_nombre(), carrera.get_idCarrera())
        self.__mycursor.execute(sql, valores)
        self.__mydb.commit()
    
    def borrar(self,carrera):
        sql = "DELETE FROM `carreras_edgar&gabriel`.carreras WHERE idcarreras = %s"
        consulta_valor = carrera.get_idCarrera()
        self.__mycursor.execute(sql,consulta_valor)
        self.__mydb.commit() 

    def __str__(self):
        pass
