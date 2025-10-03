class Carreras:
    def __init__(self, nombre: str, idCarrera = ""):
        self._nombre = nombre
        self._idCarrera = idCarrera

    def get_nombre(self):
        return self._nombre
    
    def get_idCarrera(self):
        return self._idCarrera
    
    def set_nombre(self,nombre: str):
        self._nombre = nombre

    def set_provincia(self,idCarrera: int):
        self._idCarrera = idCarrera
        
    def __str__(self):
        return f"Nombre: {self._nombre} idCarrera: {self._idCarrera}"