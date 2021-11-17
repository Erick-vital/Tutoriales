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
