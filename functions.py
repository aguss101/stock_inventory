from store import store

st=store()

def agregar():
        try:
            nombre=str(input("Nombre del producto: "))
            stock=int(input("stock de producto: "))
            if str(nombre) and int(stock):
                print("\nEl producto: {} fue añadido a la lista".format(nombre))
                return {nombre:stock}
        except ValueError as value:
            print("Debe escribir como texto al nombre y al stock en unidades enteras")
def eliminar():
    st.show_inventory()
    lista = [key.lower() for key in st.show_keys_stock()]
    listin = list(st.show_keys_stock()) 
    try:
        nombre=str(input("Elija el nombre del que desea eliminar: ")).strip()
        nombre=nombre.lower()
        if nombre in lista:
            res=input("Desea eliminar el producto: {}? \n y/n:".format(nombre.capitalize()))
            if res == "y":
                borrado = nombre.capitalize()
                posicion=lista.index(nombre)
                nombre=listin[posicion]
                if st.eliminar_productos(nombre):
                    print(f"Eliminaste el producto: {borrado}")
                    print("Esta es tu nueva lista: \n")
                    st.show_inventory()
                    input("")
            else:
                print("Cancelaste el borrado")
                input("Serás redirigido al menu principal")
        else:
            input(f"No se encontro ese producto: {nombre}")
    except TypeError as ty:
        print("Error de tipo: ",ty)
    except ValueError as valor:
        print("Objeto no encontrado: ",valor)
    except AttributeError as att:
        print("Error de atributos:", att)
    except KeyError as ke:
        print("Error de llaves: ", ke)
    except:
        print("Error, objeto no encontrado")

def choice(opcion):
    if opcion >= 0 and opcion < 4:
        if opcion  == 1:
            st.agregar_prudcto()
        elif opcion  == 2:
            st.show_inventory()
            opcion=input("\n...Presione cualquier tecla para continuar...")
        elif opcion == 3:
            eliminar()
        elif opcion == 0:
            print("Saliendo del programa...")
    else:
        print("Error! Elija su opcion entre 0 y 3")
        opcion=input("\n...Presione cualquier tecla para continuar...")