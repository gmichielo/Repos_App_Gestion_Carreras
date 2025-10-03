from DAO_Carreras import DAO_Carreras
from Carreras import Carreras

accion_usuario = 1
accion_id = 1

DAO_carreras = None
carreras = None
usuario = None
contrasenya = None

def pedir_texto(prompt: str):
    while True:
        texto = input(prompt)
        if texto.strip() == "":
            print("\033[31mUsuario inválido: no puede estar vacío ni contener solo espacios. Intenta otra vez.\033[0m")
            continue
        return str(texto)

def pedir_contrasena(prompt: str) -> str:
    while True:
        pwd = input(prompt)
        if pwd.strip() == "":
            print("\033[31mContraseña inválida: no puede estar vacía ni contener solo espacios. Intenta otra vez.\033[0m")
            continue
        return pwd
    
def verificacion_idcarrera_existente(id_buscar):
    indice_columna = 0
    for fila in carreras:
        if fila[indice_columna] == id_buscar: return True
    return False
        
def creacion_carrera(nombre, id = 0):
    carrera = Carreras(nombre, id)
    return carrera

def mostrar_opciones_carreras(carrera_lista):
    formateado = ""
    if len(carreras) > 0:
        for carrera in carrera_lista:
            formateado += f"{carrera}\n"
    else: formateado = "\033[31mLa base de datos esta vacia\033[0m"
    return formateado

def mostrar_menu_acciones():
    menu = ("\033[33m1.- Añadir carrera.\n"
        "2.- Actualizar carrera.\n"
        "3.- Ver carreras.\n"
        "4.- Borrar carrer.\n"
        "0.- Salir.\033[0m\n"
    )
    return menu

print("\033[36mBienvenid@ al gestor de carreras 2000\n")
print("\033[36mPor favor siguie las instrucciones\033[0m\n")

usuario = pedir_texto("Introduce el usuario por favor: ")
contrasenya = pedir_contrasena("Introduce la contraseña por favor: ")

DAO_carreras = DAO_Carreras(usuario, contrasenya)
DAO_carreras.connect()

if DAO_carreras.get_conexion() == True: carreras = DAO_carreras.ver()
else: print("\033[31mConexion no hecha\033[0m")

while accion_usuario != 0 and DAO_carreras != None and DAO_carreras.get_conexion() == True:

    print(mostrar_menu_acciones())

    try:
        accion_usuario = int(input(" Elige una opción: ").strip())
    except ValueError:
        print("\033[31mOpción inválida, escribe un número.\033[0m")
        continue

    if accion_usuario > 4 or accion_usuario < 0:
        print("\033[31mOpción inválida, seleccione un numero del menu.\033[0m")
        continue

    if accion_usuario == 1:
        accion_nombre_carrera = input("Introduce el nombre de la carrera: ")

        while (accion_nombre_carrera.isdigit() == True) or not accion_nombre_carrera.strip().isalnum():
            accion_nombre_carrera = input("\033[31mNombre no valido, Elige uno nuevo: \033[0m")
        
        nueva_carrera = creacion_carrera(accion_nombre_carrera)
        DAO_carreras.añadir(nueva_carrera)
        carreras = DAO_carreras.ver()

        print(f"\n\033[32mCarrera: {carreras[-1]} creada con exito\033[0m\n")

    elif accion_usuario == 2:
        print("\n" + mostrar_opciones_carreras(carreras))
        
        if len(carreras) > 0:
            accion_id = input("Introduce el id de la carrera a cambiar: ")

            while (accion_id.isdigit() == False) or (int(accion_id) <= 0) or not verificacion_idcarrera_existente(int(accion_id)) :
                accion_id = input("\033[31mEsa id no existe, Elige una nueva: \033[0m")

            accion_nombre_carrera = input("Introduce el nuevo nombre de la carrera: ")

            while (accion_nombre_carrera.isdigit() == True) or not accion_nombre_carrera.strip().isalnum():
                accion_nombre_carrera = input("\033[31mNombre no valido, Elige uno nuevo: \033[0m")

            nueva_carrera = creacion_carrera(accion_nombre_carrera,accion_id)
            DAO_carreras.actualizar(nueva_carrera)
            carreras = DAO_carreras.ver()

            print(f"\n\033[32mCarrera: {accion_id} actualizada con exito con exito\033[0m\n")

    if accion_usuario == 3:
            print(mostrar_opciones_carreras(carreras))

    elif accion_usuario == 4:
        print("\n" + mostrar_opciones_carreras(carreras))
        if len(carreras) > 0:
            accion_id = input("Introduce el id de la carrera a borrar: ")

            while (accion_id.isdigit() == False) or (int(accion_id) <= 0) or not verificacion_idcarrera_existente(int(accion_id)) :
                accion_id = input("\033[31mEsa id no existe, Elige una nueva: \033[0m")

            nueva_carrera = creacion_carrera("Carrera Borrar", [int(accion_id)])
            DAO_carreras.borrar(nueva_carrera)
            carreras = DAO_carreras.ver()

            print(f"\n\033[32mCarrera: {accion_id} borrada con exito con exito\033[0m\n")


print("\033[36mHazta luego\n\033[0m")