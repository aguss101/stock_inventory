import functions
class store:
    def __init__ (self):
        self.productos={"Iphone":100, "Samsung":90, "Fundas":90, "Motorola":20, "Xiaomi": 15 }
    def show_inventory(self):
        lista=self.productos
        for product in lista.items():
            print(f"- {product[0]}: {product[1]}")
    def inventory(self):
        return self.productos
    def agregar_prudcto(self):
        self.productos.update(functions.agregar())
        #.update(agregar())
"""
    def actualizar_producto(self):
        actualizar()

    def ver_productos(self):
        ver()

    def eliminar_productos(self):
        eliminar()
"""
