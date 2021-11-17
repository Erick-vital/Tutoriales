# Punteros en go 
Un puntero en Go es una variable que apunta y puede acceder a la dirección en memoria de otra variable.

## Entendiendo los punteros
cada variable se compone de 4 elementos
<table class="default">
  <tr>
    <td><b>nombre</b></td>
    <td><b>tipo</b></td>
    <td><b>direccion en memoria</b></td>
    <td><b>valor<b/>
  </tr>
  <tr>
    <td>numero</td>
    <td>int</td>
    <td>0xc001</td>
    <td>5</td>
  </tr>
   <tr>  
    <td>puntero</td>
    <td>*int</td>
    <td>0xc002</td>
    <td>0Xc001</td>
   </tr>
</table>
  
  Para saber la direccion en memoria de una variable usamos el operador **&** antes de la misma
  
  **Declarar un puntero:**
  ```
  // primero declaramos la variable para el puntero
  var nombre string = "erick"
  // usamos el mismo tipo de dato que la variable a apuntar con el operador '*'
  var puntero *string = &nombre
  ```
  Para obtener el valor de la variable a la que apunta el puntero(**dereferenciar**), debemos usar el operador * antes de la variable puntero   
  ejemplo:   
  ```
  fmt.Println(*puntero)
  // el output sera "erick" el cual es el valor de la variable nombre
  
  //tambien podemos cambiar el valor del puntero
  *puntero = "jose"
  ```
  
  
  
