"""
Actividad III: Dijktsra

Autor: Ruben Andree Barba Magdaleno     Registro: 20310399
Grado y Grupo: 6 F1               Clase: Inteligencia Artificial
"""

import heapq

def dijkstra(graph, start, end):
    distances = {node: float('inf') for node in graph}  # distancia inicial a cada nodo es infinita
    distances[start] = 0  # distancia al nodo de inicio es cero
    visited = {}  # nodos visitados y sus distancias
    queue = [(0, start)]  # cola de prioridad de nodos por visitar

    while queue:
        # obtenemos el nodo con la menor distancia desde el inicio
        (dist, node) = heapq.heappop(queue)

        if node in visited:
            continue  # ya visitado, pasamos al siguiente nodo

        visited[node] = dist  # agregamos el nodo visitado y su distancia

        if node == end:
            break  # hemos llegado al nodo de destino

        for neighbor, weight in graph[node].items():
            if neighbor not in visited:
                new_distance = dist + weight
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    heapq.heappush(queue, (new_distance, neighbor))

    return visited

graph = {
    'A': {'B': 2, 'F': 1},
    'B': {'A': 2, 'D': 2, 'E': 4, 'C': 2},
    'C': {'B': 2, 'E': 3, 'H': 1},
    'D': {'B': 2, 'E': 4, 'F': 3},
    'E': {'D': 4, 'B': 4, 'C': 3},
    'F': {'A': 1, 'D': 3, 'G': 5},
    'G': {'F': 5, 'E': 7, 'H': 6},
    'H': {'C': 1, 'G': 6}
}

while True:
    print("q. Salir")
    start = input("Ingrese el nodo de inicio: ")
    end = input("Ingrese el nodo de fin: ")
    if start == 'q':
        break
    elif start in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        if end in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
            path = dijkstra(graph, start, end)
            print(path)
    else:
        print("Nodo inválido, intente de nuevo.")
