from DAO_Carreras import DAO_Carreras
from Carreras import Carreras

accion_usuario = 1
accion_id = 1

DAO_carreras = DAO_Carreras("DAO_BD")
carreras = DAO_carreras.ver()

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
    for carrera in carrera_lista:
        formateado += f"{carrera}\n"
    return formateado

def mostrar_menu_acciones():
    menu = ("\033[33m1.- Añadir carrera.\n"
        "2.- Actualizar carrera.\n"
        "3.- Ver carreras.\n"
        "4.- Borrar carrer.\n"
        "0.- Salir.\033[0m\n"
    )
    return menu

print("\033[36mBienvenid@ al gestor de carreras 200\n¿Que deseas hacer?\n")

while accion_usuario != 0:

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

        print(f"\nCarrera: {carreras[-1]} creada con exito\n")

    elif accion_usuario == 2:
        print("\n" + mostrar_opciones_carreras(carreras))
        accion_id = input("Introduce el id de la carrera a cambiar: ")

        while (accion_id.isdigit() == False) or (int(accion_id) <= 0) or not verificacion_idcarrera_existente(int(accion_id)) :
            accion_id = input("\033[31mEsa id no existe, Elige una nueva: \033[0m")

        accion_nombre_carrera = input("Introduce el nuevo nombre de la carrera: ")

        while (accion_nombre_carrera.isdigit() == True) or not accion_nombre_carrera.strip().isalnum():
            accion_nombre_carrera = input("\033[31mNombre no valido, Elige uno nuevo: \033[0m")

        nueva_carrera = creacion_carrera(accion_nombre_carrera,accion_id)
        DAO_carreras.actualizar(nueva_carrera)
        carreras = DAO_carreras.ver()

    if accion_usuario == 3:
        print(mostrar_opciones_carreras(carreras))

    elif accion_usuario == 4:
        print("\n" + mostrar_opciones_carreras(carreras))
        accion_id = input("Introduce el id de la carrera a borrar: ")

        while (accion_id.isdigit() == False) or (int(accion_id) <= 0) or not verificacion_idcarrera_existente(int(accion_id)) :
            accion_id = input("\033[31mEsa id no existe, Elige una nueva: \033[0m")

        nueva_carrera = creacion_carrera("Carrera Borrar",accion_id)
        DAO_carreras.actualizar(nueva_carrera)
        carreras = DAO_carreras.ver()


print("\033[36mHazta luego\n\033[0m")