"""Desarrollar un programa que procese un conjunto de registros de ventas (por ejemplo, listas de
diccionarios) para extraer información relevante. Los estudiantes deberán aplicar funciones
internas como map, filter y reduce para transformar y filtrar los datos, calculando totales y
promedios. Este ejercicio busca que los estudiantes identifiquen y aprovechen las
funcionalidades nativas de Python para la manipulación eficiente de estructuras de datos."""

# Lista de diccionarios con los registros de ventas en córdobas
ventas = [
    {"producto": "Laptop", "categoria": "Electrónica", "precio": 24500, "cantidad": 5},
    {"producto": "Smartphone", "categoria": "Electrónica", "precio": 19250, "cantidad": 10},
    {"producto": "Tablet", "categoria": "Electrónica", "precio": 8600, "cantidad": 7},
    {"producto": "Silla", "categoria": "Muebles", "precio": 3000, "cantidad": 4},
    {"producto": "Escritorio", "categoria": "Muebles", "precio": 7500, "cantidad": 3},
    {"producto": "Monitor", "categoria": "Electrónica", "precio": 4500, "cantidad": 6},
    {"producto": "Libro", "categoria": "Papelería", "precio": 360, "cantidad": 20},
    {"producto": "Cuaderno", "categoria": "Papelería", "precio": 100, "cantidad": 15}
]

# Calcular el total de ventas por producto
ventas_totales = []
for v in ventas:
    total = v["precio"] * v["cantidad"]
    ventas_totales.append({"producto": v["producto"], "total": total})

# Filtrar las ventas de la categoría "Electrónica"
ventas_electronica = list(filter(lambda v: v["categoria"] == "Electrónica", ventas))

# Calcular el total de ingresos
total_ingresos = 0
for v in ventas:
    total_ingresos += v["precio"] * v["cantidad"]

# Calcular el promedio de ventas por categoría
categorias = set(v["categoria"] for v in ventas)
promedios = {}
for categoria in categorias:
    ventas_categoria = [v for v in ventas if v["categoria"] == categoria]
    total_categoria = sum(v["precio"] * v["cantidad"] for v in ventas_categoria)
    promedio = total_categoria / len(ventas_categoria)
    promedios[categoria] = promedio

# Imprimir resultados
print("Total de ventas por producto:")
for venta in ventas_totales:
    print(venta)

print("\nTotal de ingresos:", "C$", total_ingresos)

print("\nPromedio de ventas por categoría:")
for categoria, promedio in promedios.items():
    print(f"{categoria}: C$ {promedio:.2f} ")