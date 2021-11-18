# Estructuras
en Go la estructuras son parecidas a las **clases** de POO, el nombre de las estructuras
son su propio tipo de dato

**Declarar una estructura:**
```
// declaramos una estructura de tipo Persona, fuera de la funcion main
type Persona struct {
  // estos campos serian como los atributos
  nombre, apellido string
  edad int
}
```

**Declarar objetos**
```
// 2 ejemplos de como declarar objetos de el typo Persona
// los objetos se deben declarar dentro de funciones ya sea main u otra

// ejemplo 1
var p2 Persona = Persona{"jenifer", "salomon", 24}

// ejemplo 2
p1 := Persona{"jose", "perez", 33}
```

## Metodos
Un metodo es una funcion ligada a una estructura.   

Los metodos en go son como cualquien metodo de programacion orientada a objetos, solo que los metodos funcionan
sobre las **estructuras** en vez de sobre las clases

**Declarar un metodo:**   
tomando como ejemplo la estructura anterior Persona, creamos un metodo correr
```
// despues especificamos la estructura que se ligara el metodo
// nombre del metodo y al final el valor a retornar del metodo
func (Persona) correr() string {
  return "la persona esta corriendo"
}
```
ejemplo de un metodo que cambia el nombre de la persona      
```
// el self referencia a los atributos de la estructura, pero puede llevar cualquier nombre
// agregamos la estructura en forma de puntero con el operador *
// agregamos nombre del metodo y su argumento nuevo nombre
func (self *Persona) cambiar_nombre(nuevo_nombre string) {
  self.nombre = nuevo_nombre
}
```

Siempre que queramos modificar atributos del objeto en un metodo debemos referenciar la estructura
en forma de puntero dentro del metodo, para esto usamos el operador *

## Programacion orientada a objetos en Go
En go existe debate sobre si es orientado a objetos o no, mientras tanto existen estructuras que funcionan
de forma similar a las POO

El siguiente texto fue copiado de [aqui](https://github.com/GoesToEleven/GolangTraining/blob/master/20_struct/00_object-oriented/notes.txt)

Go is Object Oriented

(1) Encapsulation   
state ("fields")   
behavior ("methods")   
exported / un-exported

(2) Reusability   
inheritence ("embedded types")

(3) Polymorphism   
interfaces   

(4) Overriding   
"promotion"   

//////////////
Traditional OOP

Classes
-- data structure describing a type of object   
-- you can then create "instances"/"objects" from the class/blue-print   
-- classes hold both:   
==== state / data / fields   
==== behavior / methods   
-- public / private   

Inheritence   

//////////////
In Go:
- you don't create classes, you create a type
- you don't instantiate, you create a value of a type
