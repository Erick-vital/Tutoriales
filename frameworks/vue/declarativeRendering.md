# Declarative Rendering

La caracteristica principal de vue es el renderizado declarativo o
**declarative rendering**

declaramos una variable dentro del componente
```
createApp({
  data() {
    return {
      message: 'Hello World!'
    }
  }
})
```

y ahora dentro del template la variable se renderiza de forma dinamica

```
<h1>{{ message }}</h1>
```

## Attribute Bindings  
ligado de atributos o attribute binding, en vue usamos las llaves **{}** para dar valor 
a un texto de la plantilla pero para ligarlo a un atributo usamos la directiva **v-bind**

```
<div v-bind:id="dynamicId"></div>
```
En este ejemlo usamod la variable del componente "dinamicId" para ligarlo al valor del id
