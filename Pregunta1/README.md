# Lo siento por el desorden

## LA C FUE MI PROYECTO DE ALGOS 3 :)))))))))))))))))))))))))

## Usando Java (POR FIN)

### i

En java todo funciona con objetos, vamos a ver lo que ofrece Java


1.- Constructores: Se declaran dentro de las clases y se llaman al crear un nuevo objeto, retorna void y permite sobrecarga

2.- Metodos: Son funciones que declaramos dentro de una clase y operan dentro de la clase, algo super potente es que pueden ser de instancia o estatico (usando la palabra reservada static)

3.- Campos: Son variables que guardan el estado de un objeto, se declaran dentro del objeto y pueden ser de instancia o estaticos (compartidos entre todos los objetos de la clase)

### ii
Java utiliza dos enfoques para el manejo de memoria:

1.- Explicito (new/delete): Se utiliza el operador new para asignar memoria para un nuevo objeto.

2.- Implicito (recolector de basura): Java recolecta los objetos que no se van a llamar y libera la memoria

### iii
Java utiliza asociacion dinamica de metodos a traves del polimorfismo. Entonces, la seleccion del metodo adecuado se hace en tiempo de ejecucion, no en tiempo de compilacion 

Se puedes alterar la asociacion utilizando static (para asociacion estatica).

### iv

1.- Herencia: Java permite la herencia simple (una clase puede heredar de una sola clase) pero soporta la implementación de multiples interfaces para simular la herencia multiple, ejemplo

```java
public class Estudiante extends Persona implements Nadador, Estudioso 
```

2.- Polimorfismo Parametrico: Java soporta esto a traves de los generics, permitiendo que clases y metodos operen sobre tipos parametrizados.


3.- Manejo de Varianza: Con los generics, se puede usar comodines para manejar varianzas.