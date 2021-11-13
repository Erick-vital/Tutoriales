# arrays y slices

## arrays
los arrays es una colecion de elementos en mememoria el cual todos sus elementos son de un tipo de dato    

declarar arreglos
```
// areglo de tamaño 10 elementos
var numeros[10] int
```
 y damos valor a los elementos especificando su indice y su valor
 ```
 numeros[0] = 1
 ```
 
 tambien podemos declarar un array especificando el valor de cada elemetno
 
 ```
 nombres := [3]string{"erick", "alejandro", "sanchez"}
 ```
 
 ### recorrer el array
 ejemplo de la forma clasica de recorrer un array usando un bucle for
 ```
for i:=0; i<len(nombres); i++{
  fmt.Println(nombres[i])
}
```


