def ordenamiento_seleccion(lista):
    n = len(lista) # 7
    for i in range(n): # 0 - 6
        min_idx = i # 0 
        for j in range(i + 1, n): # 6
            if lista[j] < lista[min_idx]: #  42 < 7
                min_idx = j # 5
        lista[i], lista[min_idx] = lista[min_idx], lista[i] # 0 = 22, 5 = 7     =    5 = 7, 0 = 22    //  # [7, 11, 99, 88, 9, 22, 42]
    return lista

def busqueda_binaria(lista, objetivo):
    izquierda = 0 # 
    derecha = len(lista) - 1 # 

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2  # 
        if lista[medio] == objetivo: # 
            return medio # 2
        elif lista[medio] < objetivo: # 
            izquierda = medio + 1 # 
        else:
            derecha = medio - 1 # 

    return -1

numeros = [22, 11, 99, 88, 9, 7, 42]
print("Lista original:", numeros)

ordenada = ordenamiento_seleccion(numeros.copy())
print("Lista ordenada:", ordenada)

valor = int(input("Ingrese un número a buscar: "))
resultado = busqueda_binaria(ordenada, valor) # 

if resultado != -1:
    print(f"El número {valor} fue encontrado en la posición {resultado}.")
else:
    print(f"El número {valor} no está en la lista.")

