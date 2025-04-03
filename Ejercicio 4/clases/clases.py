class Inventario:
    def __init__(self):
        self.items = []
    
    def agregar_item(self, item):
        self.items.append(item)
        print(f"\nEl artículo {item.nombre} se ha agregado al almacén")
    
    def eliminar_item(self, id_item):
        for item in self.items:
            if item.codigo == id_item:
                self.items.remove(item)
                print(f"\nEl artículo {item.nombre} se ha eliminado del almacén")
                return
        print(f"\nNo se encontró el artículo con el código {id_item}")
    
    def buscar_item(self, id_item):
        for item in self.items:
            if item.codigo == id_item:
                return item
        print(f"\nEl artículo con el código {id_item} no se ha encontrado")
        return None
    
    def mostrar_inventario(self):
        print("Contenido del almacén:")
        for item in self.items:
            print(f"\nCódigo: {item.codigo}, Nombre: {item.nombre}, Precio: {item.precio}, Cantidad: {item.stock}")


class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock