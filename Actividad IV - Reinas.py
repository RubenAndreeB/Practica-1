"""
Actividad IV: Reinas

Instrucciones
    Implemente el algoritmo adjunto.

Autor: Ruben Andree Barba Magdaleno     Registro: 20310399
Grado y Grupo: 6 F1               Clase: Inteligencia Artificial
"""

def cuatro_reinas(fila):
    k = 1
    fila[0] = 0
    while k > 0:
        fila[k-1] = fila[k-1] + 1
        while (fila[k-1] <= 4) and conflicto(fila, k):
            fila[k-1] = fila[k-1] + 1
        if fila[k-1] <= 4:
            if k == 4:
                return True
            else:
                k = k + 1
                fila[k-1] = 0
        else:
            k = k - 1
    return False

def conflicto(fila, k):
    for i in range(k-1):
        if (fila[i] == fila[k-1]) or (fila[i] - fila[k-1] == i - (k-1)) or (fila[i] - fila[k-1] == (k-1) - i):
            return True
    return False

fila = [0, 0, 0, 0]
solucion = cuatro_reinas(fila)
if solucion:
    print("Hay solución:")
    for i in range(4):
        print("Reina N-{}: fila {}".format(i+1, fila[i]))
else:
    print("No hay solución.")
