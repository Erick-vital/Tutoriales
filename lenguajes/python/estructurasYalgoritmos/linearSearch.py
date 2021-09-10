def linear_search(objetivo):
    lista = [1, 4 , 7, 2, 5, 3]

    for i in lista:
        if i == objetivo:
            print('objetivo encontrado {objetivo}'.format(objetivo=objetivo))
            break

    print(lista)
    if objetivo not in lista:
        print('{objetivo} no esta en la lista'.format(objetivo=objetivo))


entrada = int(input('escribe numero a buscar en la lista: '))

linear_search(entrada)
