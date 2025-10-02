from DAO_Carreras import DAO_Carreras

accion_usuario = 1

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

print("\033[36mHazta luego\n\033[0m")