# arrays y slices

## Arrays
los arrays es una colecion de elementos en memoria el cual todos sus elementos son de un tipo de dato y ademas tienen
un tamano definido

**declarar arreglos**
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

## Slices
un slice nace de un **array** y apunta hacia el, como su nombre lo indica "slice" o **rebanada** es una porcion   
o rebanada de un arreglo.  

Un slice a diferencia de un arreglo si puede incrementar su tamaño y agregar nuevos elementos

**Declarar slices**

Declarar slices apartir de un arreglo:
```
miArray := [10]int{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
miSlice := miArray[2:4]
```
recuerda que al indexear la creacion de slice se agrega el primer indice pero el segundo retrocede uno, por
lo que el ouput de ese slice seria {2, 3}

Declarar slice sin aparente uso de arreglo:
```
miSlice2 = []int{1, 2, 3}
```
parece en este ejemplo no se usa arreglo para declarar el slice pero un arreglo igual que el slice
se crea para servir de base del slice 

Forma recomendada de declarar un array:
```
// Crea un slice de tipo int con longuitud de 3
miSlice3 := make([]int, 3)
```
esta al igual que la forma anterior crea un array por debajo, pero en este metodo podemos tener mas control del tamaño del slice


### agregando nuevos valores al slice
agregar uno o mas elementos
```
slice := make([]int, 3)
// con apppend especificamos el slice y los elementos a agregar
slice = append(slice, 1, 2)
```

