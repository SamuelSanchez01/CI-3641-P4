public class DFS extends Busqueda {

    public DFS(Grafo grafo) {
        super(grafo);
    }

    @Override
    public int buscar(int D, int H) {
        Set<Integer> visitados = new HashSet<>();
        Stack<Integer> pila = new Stack<>();
        pila.push(D);
        int explorados = 0;

        while (!pila.isEmpty()) {
            int nodo = pila.pop();
            if (nodo == H) {
                return explorados;
            }

            if (!visitados.contains(nodo)) {
                visitados.add(nodo);
                explorados++;

                for (int vecino : grafo.obtenerVecinos(nodo)) {
                    if (!visitados.contains(vecino)) {
                        pila.push(vecino);
                    }
                }
            }
        }

        return -1; //Si H no es alcanzable desde D
    }
}