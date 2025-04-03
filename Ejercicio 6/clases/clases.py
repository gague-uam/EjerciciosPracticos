class Factura:
    def __init__(self, producto, cantidades, precio, descuento):
        self.producto = producto
        self.cantidades = cantidades
        self.precio = precio
        self.descuento = descuento

    def calc_total(self):
        if self.validaciones():
            raise ValueError("No se ha podido realizar la funcion")
        else:
            return self.precio * self.cantidades * (0.01 * self.descuento)

    def reporte(self):
        return ( 
        f"Factura de {self.producto}:\n"
        f"Cantidad: {self.cantidades}\n"
        f"Precio: {self.precio:.2f}\n"
        f"Descuento: {self.descuento / 100:.2}\n"
        f"Total: {self.calc_total():.2f}" )
    
    def validaciones(self):
        if not isinstance(self.producto, str) or not self.producto.strip():
            return "El nombre del producto debe ser una cadena no vacía."
        if not isinstance(self.cantidades, (int, float)) or self.cantidades <= 0:
           return "La cantidad debe ser un número mayor a 0."
        if not isinstance(self.precio, (int, float)) or self.precio <= 0:
            return "El precio debe ser un número mayor a 0."
        if not isinstance(self.descuento, (int, float)) or not (0 <= self.descuento <= 100):
            return "El descuento debe ser un número entre 0 y 100."
    
