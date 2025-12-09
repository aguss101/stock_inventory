def agregar():
        try:
            nombre=str(input("Nombre del producto: "))
            stock=int(input("stock del producto: "))
            return {nombre:stock}
        except ValueError as value:
            print("Debe escribir como texto al nombre y al stock en unidades enteras")
def eliminar():
    f=4
    print(f)


def choice(opcion, tt):
    if opcion >= 0 and opcion < 4:
        if opcion  == 1:
            tt.agregar_prudcto()
        elif opcion  == 2:
            tt.show_inventory()
            opcion=input("\n...Presione cualquier tecla para continuar...")
        elif opcion == 3:
            eliminar()
        elif opcion == 0:
            print("Saliendo del programa...")
    else:
        print("Opcion invalida! Elija su opcion entre 0 y 3")
