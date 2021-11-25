# Clases
las clases suelen se suelen crear en visual estudio como modulos por asi decirlo esot como buena practica, pero se pueden crear
dentro del modulo principal como el siguiente ejemplo    

Definir una clase:
```
class Circulo{
		const double pi = 3.1416;
		double radio;
		
    // metodo constructor
		public Circulo(double radio){
			this.radio = radio;
		}
		
    // public es el alcanze o scoope del metodo
		public double area(){
			return pi * this.radio * this.radio;
		}
	}
```

como vemos esta clase tiene su **meotodo constructor**, que es un metodo que se inicializa al crear un objeto, es como el metodo __init__ en python, en c# los
metodos constructores deben de llevar el mismo nombre de la clase

# Objetos
instaciar una clase o crear un objeto

Instanciamos la clase circulo:
```
Circulo c1 = new Circulo(4);
```
