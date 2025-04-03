"""Se requiere que los estudiantes diseñen un módulo independiente que contenga
implementaciones de algoritmos de ordenamiento simples (bubble sort). El objetivo es que, a
partir de una función principal, se invoquen los métodos del módulo para ordenar una lista de
números y demostrar la correcta separación de responsabilidades, fomentando la modularidad
y la reutilización del código."""
import clases.clases as c

numeros = []
cantidad = int(input("Ingrese la cantidad de elementos a digitar: "))
for i in range(cantidad):
    numero = int(input("Ingresa un numero: "))
    numeros.append(numero)

print("Lista original:", numeros)
lista_ordenada = c.bubble_sort(numeros)
print("Lista ordenada:", lista_ordenada)

