from DAO_Carreras import DAO_Carreras
#from Carreras import Carreras

accion_usuario = 1
accion_id = 1

DAO_carreras = DAO_Carreras("3")
carreras = ["a"]

#def creacion_carrera():
#    carrera = Carrera()
#    return carrera

def rellenar_opciones_carreras():
    carreras_actu = []
    return carreras_actu

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

carreras = rellenar_opciones_carreras()

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
        print("Accion de Añadir")

    elif accion_usuario == 2:
        print("\n" + mostrar_opciones_carreras(carreras))
        accion_id = input("Escoge la id de la carrera a actualizar: ")

        while (accion_id.isdigit() == False) or (int(accion_id) > len(carreras)) or (int(accion_id) <= 0) :
            accion_bus = input("\033[31mEsa id no existe, Elige una nueva: \033[0m")


        carreras = rellenar_opciones_carreras()

    elif accion_usuario == 3:
        print(mostrar_opciones_carreras(carreras))

    elif accion_usuario == 4:
        print("\n" + mostrar_opciones_carreras(carreras))
        accion_id = input("Escoge la id de la carrera a borrar: ")

        while (accion_id.isdigit() == False) or (int(accion_id) > len(carreras)) or (int(accion_id) <= 0) :
            accion_bus = input("\033[31mEsa id no existe, Elige una nueva: \033[0m")


        carreras = rellenar_opciones_carreras()

print("\033[36mHazta luego\n\033[0m")