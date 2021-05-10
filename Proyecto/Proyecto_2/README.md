### Características

##Proyecto 2 - Algoritmos BFS y DFS
Utilizando la biblioteca de grafos desarrollada en el Proyecto1, implementar los algoritmos BFS y DFS (recursivo e iterativo) de tal forma que dado un nodo fuente(s), calculen el árbol inducido por los algoritmos mencionados; es decir, desarrollar los métodos en la clase Grafo:
def BFS(self, s):
def DFS_R(self, s):
def DFS_I(self, s):

Entregables:
Repositorio GIT (distinto al del primer proyecto)
Archivos de grafos generados. Tres por cada generador (con 30, 100 y 500 nodos).
Archivos de grafos calculados. Tres por cada grafo generado (un BFS y dos DFS).
Imágenes de la visualización de cada grafo (generados y calculados).

## Entrega
La rama Proyecto2 cuenta con la carpeta que cumple con lo solicitado, en dicha carpeta encontrará las siguientes carpetas:
- A_BFS: con los 18 archivo gv de los arboles generados con el algoritmo de busqueda a lo ancho
-  A_BFS_imagen: con las 18 imagenes generadas utilizando los archivos de la carpeta A_BFS, utilizando el programa Gephi
- A_DFSi: con los 18 archivo gv de los arboles generados con el algoritmo de busqueda en profundidad iterativo
-  A_DFSi_imagen: con las imagenes generadas utilizando los archivos de la carpeta A_DFSi, utilizando el programa Gephi
- A_DFSr: con los archivo gv de los arboles generados con el algoritmo de busqueda en profundidad recursivo
-  A_DFSr_imagen: con las imagenes generadas utilizando los archivos de la carpeta A_DFSr, utilizando el programa Gephi
-  Codigo: codigo .py compatible con Python 3.6
-  Grafos: Archivos gv generados con el código desarrollado para el Proyecto1
-  Grafos_imagen: con las imagenes generadas utilizando los archivos de la carpeta Grafos, utilizando el programa Gephi

### Ejemplos de imagenes generadas
Generado con Modelo de BarabasiAlbert, 100 nodos:
![](https://github.com/cynthiayustis/AlgoritmosCIC/blob/Proyecto2/Proyecto/Proyecto_2/Grafos_imagen/BarabasiAlbert_100.png?raw=true)


Generado del modelo de BarabasiAlbert arbol generado con el algoritmo de busqueda en profundidad iterativo, 100 nodos:
![](https://github.com/cynthiayustis/AlgoritmosCIC/blob/Proyecto2/Proyecto/Proyecto_2/A_DFSi_imagen/BarabasiAlbert3_DFSi.png?raw=true)