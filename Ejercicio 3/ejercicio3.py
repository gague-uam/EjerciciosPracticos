from models.models import busqueda_binaria, busqueda_lineal

lista = [34, 7, 23, 32, 5, 62, 78, 1, 45, 90]

def main():
    print("Bienvenido al programa de busqueda.")
    print(f"Lista predefinida: {lista}")

    print("Ingrese el numero que desea buscar:")
    numero = int(input())

    print("Seleccione el metodo de busqueda:")
    print("1. Busqueda Binaria")
    print("2. Busqueda Lineal")
    opcion = int(input())

    if opcion == 1:
        # Ordenar la lista para la búsqueda binaria
        lista_ordenada = sorted(lista)
        print(f"Lista ordenada para busqueda binaria: {lista_ordenada}")
        resultado = busqueda_binaria(lista_ordenada, numero, 0, len(lista_ordenada) - 1)
        if resultado != -1:
            print(f"El numero {numero} fue encontrado en la posicion: {resultado+1}")
        else:
            print(f"El numero {numero} no fue encontrado en la lista.")
    elif opcion == 2:
        resultado = busqueda_lineal(lista, numero)
        if resultado != -1:
            print(f"El numero {numero} fue encontrado en la posicion: {resultado+1}")
        else:
            print(f"El numero {numero} no fue encontrado en la lista.")
    else:
        print("Opción no valida. Por favor, seleccione 1 o 2.")

if __name__ == "__main__":
    main()