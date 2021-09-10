""" implentacion de algoritmo de busqueda binaria
    
    el algoritmo de busqueda binaria tiene el proposito de buscar un numero
    dada una lista ordenada, y este a diferencia de la busqueda lineal es mucho
    mas rapido
"""

def binary_search(objetivo):
    lista = [4, 18, 33, 22, 1, 55, 40, 18, 11]

    # Primero ordenamos la lista
    lista = sorted(lista)
    mitad = round(len(lista)/2)
    inicio = 0
    final = len(lista)-1
    contador = 1

    while objetivo != lista[mitad]:
        if objetivo < lista[mitad]:
            final = mitad
            mitad = round(final/2)
        elif objetivo > lista[mitad]:
            inicio = mitad
            mitad = int(round(final-inicio)/2+inicio)
        
        if contador >= len(lista):
            print('elemento no encontrado')
            break
        contador +=1 
    else:
        print(lista)
        print('{objetivo} encontrado en lista'.format(objetivo=objetivo) )



binary_search(22)


