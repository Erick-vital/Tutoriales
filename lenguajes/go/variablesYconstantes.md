## Variables
go es un lenguaje tipado por lo que podemos definir el tipo de dato de una variable al declararla, aunque esto no es obligatorio en go por que    
tenemos distintas formas de declarar una variable.   

### Declarar variables

Declarar variable sin inciar un valor, no asigna un valor aun a la variable
```
var i int
```

Declar variable larga asignando un valor
```
var i int = 5
```

Declarar variable de forma corta, aqui no especificamos un tipo de dato por lo que go asigna uno de forma automatica
```
i := 5
```

### Declarar Constantes
se declara una constante con la palabra reservada **const**    

Declarar constante sin definir tipo
```
const pi = 3.14
```

Declarar constate definiendo tipado

```
const pi float32 = 3.14
```

