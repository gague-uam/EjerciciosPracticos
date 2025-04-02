"""Se requiere que los estudiantes diseñen un módulo independiente que contenga
implementaciones de algoritmos de ordenamiento simples (bubble sort). El objetivo es que, a
partir de una función principal, se invoquen los métodos del módulo para ordenar una lista de
números y demostrar la correcta separación de responsabilidades, fomentando la modularidad
y la reutilización del código."""

def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista

numeros = []
cantidad = int(input("Ingrese la cantidad de elementos a digitar: "))
for i in range(cantidad):
    numero = int(input("Ingresa un numero: "))
    numeros.append(numero)

print("Lista original:", numeros)
lista_ordenada = bubble_sort(numeros)
print("Lista ordenada:", lista_ordenada)

