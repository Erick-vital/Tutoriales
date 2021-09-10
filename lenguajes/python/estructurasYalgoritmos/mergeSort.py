def merge(array):
    mitad = array[:len(array)//2]
    mitad2 = array[len(array)//2:]

    print('{mitad} \n {mitad2}'.format(mitad=mitad, mitad2=mitad2))

merge([1, 2, 3, 4, 5])


