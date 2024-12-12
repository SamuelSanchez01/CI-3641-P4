public class BFS extends Busqueda {

    public BFS(Grafo grafo) {
        super(grafo);
    }

    @Override
    public int buscar(int D, int H) {
        Set<Integer> visitados = new HashSet<>();
        Queue<Integer> cola = new LinkedList<>();
        cola.add(D);
        int explorados = 0;

        while (!cola.isEmpty()) {
            int nodo = cola.poll();
            if (nodo == H) {
                return explorados;
            }

            if (!visitados.contains(nodo)) {
                visitados.add(nodo);
                explorados++;

                for (int vecino : grafo.obtenerVecinos(nodo)) {
                    if (!visitados.contains(vecino)) {
                        cola.add(vecino);
                    }
                }
            }
        }

        return -1; // Si H no es alcanzable desde D
    }
}