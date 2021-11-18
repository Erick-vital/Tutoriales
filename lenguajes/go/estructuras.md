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
func (self Persona)
```

