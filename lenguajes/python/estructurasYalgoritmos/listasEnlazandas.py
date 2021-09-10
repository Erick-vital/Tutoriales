class Nodo:
    def __init__(self, dato, puntero):
        self.dato = dato
        self.puntero = puntero



class ListaEnlazada:
    def __init__(self):
        self.primero = None
        self.cola = 0

    def agregar_dato(self, datos):
        nodo = Nodo(datos, None)
        if self.primero == None:
            self.primero = nodo
        else:
            actual = self.primero 

            while actual.puntero != None:
                actual = actual.puntero
            actual.puntero = nodo
        
        self.cola +=1
        return nodo.dato

    def longitud(self):
        return self.cola
        

    def imprimir(self):
        actual = self.primero

        while actual.puntero != None:
            print(actual.dato)
            actual = actual.puntero
        print(actual.dato)

    def remover(self, key):
        actual = self.primero

        # Si el nodo actual no esta vacio y ademas tiene el dato que buscamos
        if actual and actual.dato == key:
            self.primero = actual.puntero
            actual = None
            return 

        anterior = None

        while actual.dato != key:
            anterior = actual
            actual = actual.puntero


        anterior.puntero = actual.puntero
        actual = None




lista = ListaEnlazada()
