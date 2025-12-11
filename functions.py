def agregar():
    try:
        nombre=str(input("Nombre del producto: ")).strip()
        stock=int(input("stock de producto: "))
        
        print("\nEl producto: {} fue añadido a la lista".format(nombre))
        return {nombre:stock}
    except ValueError as value:
        print("Error: El nombre debe ser unicamente texto y el stock expresado en unidades")

def actualizar(st):
    try:
        st.show_inventory()
        lista_llaves = [key.lower() for key in st.show_keys_stock()]
        lista = list(st.show_keys_stock())
        nombre=str(input("Que producto de la lista desea actualizar?").strip())
        nombre=nombre.lower()
        if nombre in lista_llaves:
            res=input("Desea actualizar el stock del producto: {}? \n y/n:".format(nombre.capitalize()))
            if res == "y":
                stock=int(input("Ingrese el stock actualizado del producto: "))
                posicion=lista_llaves.index(nombre)
                clave_final = lista[posicion]
                if st.actualizar_productos(clave_final, stock):
                    print(f"El producto: {nombre.capitalize()} actualizo su stock a: {stock}")
                    print("Esta es tu nueva lista: \n")
                    st.show_inventory()
                    input("")
                else:
                    print("Error en la funcion")
            elif res != "y" and res != "n":
                print("Opcion invalida")
                input("Serás redirigido al menu principal")
            else:
                print("Cancelaste la actualizacion del stock")
                input("Serás redirigido al menu principal")
        else:
            print("No se encontró ese producto")
    except ValueError as value:
        print("Error: Exprese el stock en unidades")

def eliminar(st):
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
            input(f"No se encontró ese producto: {nombre}")
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

def choice(opcion, st):
    if opcion >= 0 and opcion < 5:
        if opcion  == 1:
            st.agregar_prudcto()
        elif opcion  == 2:
            st.show_inventory()
            opcion=input("\n...Presione cualquier tecla para continuar...")
        elif opcion == 3:
            eliminar(st)
        elif opcion == 4:
            actualizar(st)
        elif opcion == 0:
            print("Saliendo del programa...")
    else:
        print("Error! Elija su opcion entre 0 y 4")
        opcion=input("\n...Presione cualquier tecla para continuar...")