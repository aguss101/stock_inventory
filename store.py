import functions
class store:
    def __init__ (self):
        self.productos={"Iphone":100, "Samsung":90, "Fundas":90, "Motorola":20, "Xiaomi": 15 }
    def show_inventory(self):
        lista=self.productos
        for product in lista.items():
            print(f"- {product[0]}: {product[1]}")

    def show_keys_stock(self):
        return self.productos.keys()
    
    def agregar_prudcto(self):
        self.productos.update(functions.agregar())
        print("Esta es su nueva lista: ")   
        self.show_inventory()
    def eliminar_productos(self, nombre):
        try:
            self.productos.pop(nombre)
            return True
        except KeyError as kk:
            print("Error al intentar eliminar: ",kk)
            return False