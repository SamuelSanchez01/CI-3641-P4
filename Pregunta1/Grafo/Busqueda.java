public abstract class Busqueda {
    protected Grafo grafo;
    
    public Busqueda(Grafo grafo) {
        this.grafo = grafo;
    }

    public abstract int buscar(int D, int H);
}