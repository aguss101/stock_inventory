from functions import choice
from store import store

st=store()

opcion=1

while opcion != 0:
    print("------------------------------------")
    print("---------MENU DE GESTION------------")
    print("------------------------------------\n")

    print("1-Agregar      --  3-Eliminar")
    print("2-Mostrar      --  4-Actualizar\n")
    print("0-Salir")
    try:
        opcion=int(input(""))
        choice(opcion, st)
    except ValueError as valor:
        print("Error! Elija su opcion entre 0 y 4")
        opcion=input("\n...Presione cualquier tecla para continuar...")