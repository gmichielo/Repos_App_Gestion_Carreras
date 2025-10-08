import mysql.connector
from mysql.connector import Error

class DAO_Carreras():
    def __init__(self, user_input: str, password_input: str):

        self.__host = "localhost"
        self.__user = user_input
        self.__password = password_input
        self.__database = "carreras_edgar_y_gabriel"
        self.__conexionHecha = False
        
    def get_conexion(self):
        return self.__conexionHecha
    
    def conectar(self):
        try:
            self.__mydb = mysql.connector.connect(
                host=self.__host,
                user=self.__user,
                password=self.__password,
                database=self.__database
            )
            self.connected = self.__mydb.is_connected()
            self.__mycursor = self.__mydb.cursor()
            self.__conexionHecha = True
        except Error as err:
            self.__mydb = None
            self.__mydb = False
            self.last_error = err

    def reconectar(self, user=None, password=None):
        if user:
            self.__user = user
        if password:
            self.__password = password
        self.conectar()
        return self.connected

    def anyadir(self, carrera):
        sql = "INSERT INTO carreras_edgar_y_gabriel.carreras (nombre) VALUES (%s)"
        val = [carrera.get_nombre()]
        self.__mycursor.execute(sql, val)
        self.__mydb.commit()

    def ver(self):
        self.__mycursor.execute("SELECT * FROM carreras")
        self._myresult = self.__mycursor.fetchall()
        return self._myresult
    
    def actualizar(self, carrera):
        sql = "UPDATE carreras_edgar_y_gabriel.carreras SET nombre = %s WHERE idcarreras = %s"
        valores = (carrera.get_nombre(), carrera.get_idCarrera())
        self.__mycursor.execute(sql, valores)
        self.__mydb.commit()
    
    def borrar(self,carrera):
        sql = "DELETE FROM carreras_edgar_y_gabriel.carreras WHERE idcarreras = %s"
        consulta_valor = carrera.get_idCarrera()
        self.__mycursor.execute(sql,consulta_valor)
        self.__mydb.commit() 

    def __str__(self):
        pass
