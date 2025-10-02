import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123456",
    database="universidad"
)

class DAO_Carreras():
    def __init__(self, password):
        self.__password = password