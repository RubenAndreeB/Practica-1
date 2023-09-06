"""
Actividad II: Busqueda en profundidad

Autor: Ruben Andree Barba Magdaleno     Registro: 20310399
Grado y Grupo: 6 F1               Clase: Inteligencia Artificial
"""

import re 
patron=re.compile(r'\W')

E={('a','b'),('a','c'),('a','g'),('b','a'),('b','d'),('b','g'),('c','a'),('c','d'),('c','e'),
    ('d','b'),('d','c'),('d','f'),('e','c'),('e','f'),('e','g'),('f','d'),('f','e'),('f','h'),
    ('g','a'),('g','b'),('g','e'),('h','f')} 

V=('a b c d e f g h')


def bus_profundidad(E,ni,V):
      nodos={'a':0,'b':1,'c':2,'d':3,'e':4,'f':5,'g':6,'h':7} 
      vi=nodos[ni]
      V=patron.split(V)
      v1=V[vi]
      Vp=[v1]
      Ep=[]
      w=v1
      padre={}
      while True:
          while True:
              arista=[(w,x) for x in V if ((w,x) in E and x not in Vp)]
              if arista==[]:
                  break
              vk=arista[0]
              Ep.append(vk)
              Vp.append(vk[1])
              padre.update({vk[1]:w})
              w=vk[1]
          if w==v1:
              print (Ep)
              break
          w=padre.get(w)

      return Ep

while True:
    vi = input("Ingrese el nodo inicial (a-h) o 'q' para salir: ")
    if vi == 'q':
        break
    elif vi in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        bus_profundidad(E, vi, V)
    else:
        print("Nodo inválido, intente de nuevo.")
