//Definamos Secuencia
public interface Secuencia<T> {
    void agregar(T elemento);
    T remover() throws Exception;
    boolean vacio();
}