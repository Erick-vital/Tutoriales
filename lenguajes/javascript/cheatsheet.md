## JAVASCRIPT
Concepto y conocimientos aprendidos de JS

## Asincrono
El codigo de javascript es asincrono, osea que no es lineal y no espera a una ejecucion a ser terminanda para ejecutar la siguiente

### Callbacks
Para eso se inventaron las callbacks lo cual nos permite correr nuestras funcinoes de forma sincrona, ya que se genera un stack de funciones
y una tiene que esperar a la otra para ser ejecutada.   

En codigo una callback se representa simplemente como una funcion que usa como parametro y llama a otra funcion.
```
// Como vemos en el ejemplo la funcion "saludar" tiene que esperar a la funcion "entradausuario" para ser ejecutada
function saludar(nombre) {
  alert('Hola ' + nombre);
}

function procesarEntradaUsuario(callback) {
  var nombre = prompt('Por favor ingresa tu nombre.');
  callback(nombre);
}

procesarEntradaUsuario(saludar);
```

### Promesas
las promesas son la evolucion de las callbacks, estas nos permiten manejar nuestro codigo de una manera mucho mas sencilla
```
// Ejemplo de promesa
let miPrimeraPromise = new Promise((resolve, reject) => {
  // Llamamos a resolve(...) cuando lo que estabamos haciendo finaliza con éxito, y reject(...) cuando falla.
  // En este ejemplo, usamos setTimeout(...) para simular código asíncrono.
  // En la vida real, probablemente uses algo como XHR o una API HTML5.
  setTimeout(function(){
    resolve("¡Éxito!"); // ¡Todo salió bien!
  }, 250);
});

miPrimeraPromise.then((successMessage) => {
  // succesMessage es lo que sea que pasamos en la función resolve(...) de arriba.
  // No tiene por qué ser un string, pero si solo es un mensaje de éxito, probablemente lo sea.
  console.log("¡Sí! " + successMessage);
});
```

Podemos hacer cadenas de promesas ejecutando un **.then** despues de otro.    

Supongamos que vamos a comprar comida a un restaurante de comida rápida, cuando terminamos de pagar por nuestra comida nos dan un ticket con un número, cuando llamen a ese número podemos entonces ir a buscar nuestra comida.

```
const ticket = getFood();

ticket
	.then(food => eatFood(food))
	.catch(error => getRefund(error));
```

## Closure
Un closure simplemente es una funcion declarada dentro de otra funcion
```
function inicia() {
  var nombre = "test"; // 'nombre' es una variable local creada por la function 'inicia'
  function muestraNombre() { // 'muestraNombre' es una function interna (un closure)
    alert(nombre); // dentro de esta function usamos una variable declarada en la function padre
  }
  muestraNombre();
}
inicia();  
```
### Porque usar closures 
**Privacidad** de los datos, esta tecnica nos permite hacer nuestro codigo mas seguro.   

Imaginemos que desde la function externa queremos acceder al valor de la variable nombre (ejemplo anterior). No vamos a poder acceder a dicho valor libremente, la única forma será a través de la function inicia() .

En otros lenguajes, un método privado es un método expuesto que tiene acceso a datos privados. En JavaScript, cualquier método expuesto definido dentro del scope del closure es privilegiado.   

Se podria decir que seria lo mismo que declarar una variable **private** en java, en este caso la variable nombre

### Objetos
un objeto tiene propiedades y metodos, se declara parecido a como es un diccionario en python, con clave y valor

```
// ejemplo de objeto
var auto = {
color: "azul",
marca: "bmw",
propietario: [
  {
    nombre_propietario: "juan",
    edad_propietario: 24,
   }],

encendido: function(){
    console.writeline("enciende el motor");
    }
};
```
    


