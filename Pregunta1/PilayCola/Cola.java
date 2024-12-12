import java.util.*;
//Inmplementamos cola
public class Cola<T> implements Secuencia<T> {
    private LinkedList<T> elementos;

    public Cola() {
        this.elementos = new LinkedList<>();
    }

    @Override
    public void agregar(T elemento) {
        elementos.addLast(elemento);
    }

    @Override
    public T remover() throws Exception {
        if (vacio()) {
            throw new Exception("La cola esta vacia manito");
        }
        return elementos.removeFirst();
    }

    @Override
    public boolean vacio() {
        return elementos.isEmpty();
    }
}