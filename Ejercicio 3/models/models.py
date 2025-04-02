def busqueda_binaria(lista, numero, inicio, fin):
    while inicio <= fin:
        medio = (inicio + fin) // 2  
        if lista[medio] == numero:
            return medio  
        elif lista[medio] < numero:
            inicio = medio + 1  
        else:
            fin = medio - 1  
    return -1  

def busqueda_lineal(lista, numero):
    for i in range(len(lista)):
        if lista[i] == numero:
            return i
    return -1

