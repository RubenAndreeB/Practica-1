"""
Examen I: Prim

Autor: Ruben Andree Barba Magdaleno     Registro: 20310399
Grado y Grupo: 6 F1               Clase: Inteligencia Artificial
"""

def prim(w, n, s):
    # v[i] = 1 si el vértice i se agrega al aem
    # v[i] = 0 si el vértice i no se agrega al aem
    for i in range (1, n+1):
        v = [0] * (n+1)
    # Se agrega el vértice s al aem
    v[s] = 1
    # se comienza con un conjunto de aristas vacío
    E = set()
    # se ponen n-1 aristas en el aem
    for i in range(1, n):
        # se agrega la arista de peso mínimo con un vértice 
        # en el aem y un vértice que no esté en el aem
        minim = float('inf')
        for j in range(1, n+1):
            if v[j] == 1:
                for k in range(1, n+1):
                    if v[k] == 0 and k in w[j] and w[j][k] < minim:
                        agregar_vértice = k
                        e = (j, k)
                        minim = w[j][k]
        
        # se pone el vértice y la arista en el aem
        v[agregar_vértice] = 1
        E.add(e)
    return E

# se establece la gráfica ponderada como un diccionario
w = {
    1: {2: 4, 3: 2, 5: 3},
    2: {1: 4, 4: 5},
    3: {1: 2, 4: 1, 5: 6, 6: 3},
    4: {2: 5, 3: 1, 6: 6},
    5: {1: 3, 3: 6, 6: 2},
    6: {3: 3, 4: 6, 5: 2}
}

# se llama a la función prim() con los parámetros adecuados
Z = prim(w, 6, 1)

# se imprime el conjunto de aristas del aem
print(Z)