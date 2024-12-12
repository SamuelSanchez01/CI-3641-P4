import java.util.*;

public class Grafo {
    private Map<Integer, List<Integer>> adyacencias;

    public Grafo() {
        adyacencias = new HashMap<>();
    }

    public void agregarArista(int origen, int destino) {
        adyacencias.putIfAbsent(origen, new ArrayList<>());
        adyacencias.get(origen).add(destino);
    }

    public List<Integer> obtenerVecinos(int nodo) {
        return adyacencias.getOrDefault(nodo, new ArrayList<>());
    }
}