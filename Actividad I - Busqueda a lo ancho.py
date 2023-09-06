"""
Actividad I: Busqueda a lo ancho

Autor: Ruben Andree Barba Magdaleno     Registro: 20310399
Grado y Grupo: 6 F1               Clase: Inteligencia Artificial
"""

from collections import deque

graph = {
    'A': ['B', 'C', 'G'],
    'B': ['A', 'D', 'G'],
    'C': ['A', 'D', 'E'],
    'D': ['C', 'B', 'F'],
    'E': ['C', 'G', 'F'],
    'F': ['E', 'D', 'H'],
    'G': ['A', 'B', 'E'],
    'H': ['F']
}

def bfs(graph, start):
    visited = set()
    queue = deque([start])  
    while queue:
        node = queue.popleft()  
        if node not in visited:
            visited.add(node)  
            print(node)  
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

print("Bienvnido al arbol de expansión con busqueda a lo ancho.")
while True:
    print("Selecciona el nodo para comenzar:")
    print("A, B, C, D, E, F, G, H")
    print("q. Salir")
    start = input("Ingrese su elección: ")
    if start == 'q':
        break
    elif start in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']:
        bfs(graph,start)
    else:
        print("Nodo inválido, intente de nuevo.")
