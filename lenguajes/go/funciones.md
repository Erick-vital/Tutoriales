# Funciones
una funcion es un bloque de codigo que puede ser reutilizado al llamar la funcion.   

En go a diferencia de python debemos declar el tipo de dato de los argumentos(si lleva argumentos) y el tipo de dato del return(si esque lleva uno)
ya que el return y los argumentos son opcionales al igual que python

**Declarar funciones:**
```
//usamos la palabra reservada fun
// una funcion donde especificamos el tipo de dato a devolver
// el tipo de dato de los parametros tambien debe especificarse
func suma(a, b int) int{
  return a +b
 }
 ```
 
 **Llamar una funcion:**
 ```
 // tenemos que llamar a nuestras funciones desde la funcion principal main
 func main(){
  suma(5, 6)
}
```

En go una funcion puede y es comun que retorne multiples valores
