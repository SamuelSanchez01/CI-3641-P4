import java.util.*;
//Implementamos pila
public class Pila<T> implements Secuencia<T> {
    private ArrayList<T> elementos;

    public Pila() {
        this.elementos = new ArrayList<>();
    }

    @Override
    public void agregar(T elemento) {
        elementos.add(elemento);
    }

    @Override
    public T remover() throws Exception {
        if (vacio()) {
            throw new Exception("La pila esta vacia manito");
        }
        return elementos.remove(elementos.size() - 1);
    }

    @Override
    public boolean vacio() {
        return elementos.isEmpty();
    }
}