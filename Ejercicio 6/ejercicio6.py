import clases.clases as c

print("Bienvenido al sistema de facturación.\n")

factura = c.Factura(
    producto = input("Ingrese el nombre del producto: "),
    cantidades = float(input("Ingrese la cantidad del producto: ")),
    precio = float(input("Ingrese el precio del producto: ")),
    descuento = int(input("Ingrese el descuento (en porcentaje, 0-100): "))
)

total = factura.calc_total()
print(f"\nEl total de la venta es: ${total:.2f}\n")
reporte = factura.reporte()
print(f"El reporte de la venta es:\n{reporte}")