
array = [5, 3, 6, 1, 2, 4]
print('desordenado {array} \n '.format(array=array))

ordenado = False
while ordenado == False:
    ordenado = True
    for i in range(0, len(array)-1):
        if array[i] > array[i + 1]:
            ordenado = False
            temp = array[i]
            array[i] = array[i + 1]
            array[i + 1] = temp

        
    
print('ordenado {array}'.format(array=array))
           

