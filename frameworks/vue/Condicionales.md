# Condicionales y bucles en vue
en vue podemos usar ya sea condifcionales o bucles dentro del html

Para condicionales usamos la directiva v-if dentro de una etiqueta
```
<h1 v-if="awesome">Vue is awesome!</h1>
```
 la etiqueta sera mostra si la variable "awesome" es true
 
 Tambien podemos usar **v-else** o **v-else-if** para detonar otra condicion
 
 ```
<h1 v-if="awesome">Vue is awesome!</h1>
<h1 v-else>Oh no 😢</h1>
 ```
 
