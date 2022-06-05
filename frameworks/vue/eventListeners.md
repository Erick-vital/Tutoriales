Para escuchar eventos dentro del DOM usamos la directiva **v-on**

```
<button v-on:click="increment">{{ count }}</button>
```

en este caso escuchamos el evento click el cual activara el metodo increment al click

```
createApp({
  data() {
    return {
      count: 0
    }
  },
  methods: {
    increment() {
      // update component state
      this.count++
    }
  }
})
```

La forma corta de escribir la directiva v-on es con un **@**

```
<button @click="increment">{{ count }}</button>
```

