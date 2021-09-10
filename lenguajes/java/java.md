## JAVA CHEATSHEET
conceptos y aprendizajes de java

### Paquetes
Un paquete es un contenedor de clases, dentro de un paquete podemos guardar
varias clases

### Esctructura de clases
```
// public es el modificador de acceso o alcance
// crear una clase

plublic class Prueba {

}
```
## Metodos
En java un metodo es una funcion de un objeto basicamente es lo mismo que un
metodo en python

**metodo void o procedimiento**
```
// este es un metodo que no retorna valores
public void metodo_procedmiento(){
    system.out.println("hola que tal");
}
```

**metodo que retorna un valor**
```
// este metodo retorna un valor, en este caso un valor de tipo int 
public int suma(int a, int b){
    int suma = a + b;
    return suma;
}
```

**sobre carga de metodos**
esto ocurre cuando tenemos dos o mas metodos con el mismo nombre, para diferenciarlos
tenemos que poner un numero diferente de parametros en cada metodo

### metodos especiales

**metodo constructor**   
es un metodo que se inicializa al instanciar el objeto, que nos sirve tambien
para instanciar los atributos de nuestro objeto
```
// No devuelve ningun valor
// Se declara con el mismo nombre de la clase
// debe declarse como publico
public class Coche {
    String color;
    String marca;
    int km

    // este es el metodo constructor
    public Coche(String color, String marca, int km){
            this.color = color;
            this.marca = marca;
            this.km = km
        }
}
```


### Objeto
Un objeto es la instancia de una clase
```
// creamos un objeto de la clase prueba
Prueba objeto_prueba = new Prueba();
```

### Encapsulamiento
primero debemos saber el alcance o modificador de acceso de un atributo

1.public: nos permite acceder al atributo desde la mimsa clase o desde otra clase del 
mismo o diferente paquete 

2.private: solo podemos acceder al atributo desde la misma clase 

**Setters y geters**
para acceder a un atributo private creamos los metodos setters y geters

```
private String atributo;

public void setAtributo(String atributo){
        this.atributo = atributo
    }

public int getAtributo() {
    return atributo
}
```

### Herencia
Es cuando una clase hereda de otra

```
// En este ejemplo la clase "Hija" hereda de la clase "Padre"
// Para que una clase here de otra se usa la palabra reservada extends
public class Hija extends Padre{
}
```

### Polimorfismo

es cuando un metodo tiene diferente comportamiento dependiendo el objeto    

Existen 3 tipos de polimorfismo

1.sobrecarga
2.parametrico
3.inclusion

