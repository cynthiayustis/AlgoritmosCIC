#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import numpy as np

class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = list()
        self.grado = 0
        self.revisado = False
        self.nivel = 0
        self.ancestro = None
        self.peso = float('inf')
    def addNode(self,nuevo_nodo):
        if not(nuevo_nodo in self.getConections()):
            self.conexiones.append(nuevo_nodo)
    def getName(self):
        return self.nombre
    def addAncestro(self,nodo_ancestro):
        self.ancestro = nodo_ancestro
    def getAncestro(self):
        return self.ancestro
    def addRevisado(self):
        self.revisado = True
    def addNivel(self,level):
        self.nivel = level
    def getNivel(self):
        return self.nivel
    def getRevisado(self):
        return self.revisado
    def getConections (self): #funcion para obtener la lista de conexiones
        return self.conexiones
    def addGrado(self):
        self.grado = self.grado + 1
    def getGrado(self):
        return self.grado
    def addPeso(self,peso):
        self.peso = peso
    def getPeso(self):
        return self.peso


# In[2]:


class Arista:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ancestro = None
        self.descendiente = None
        self.peso = 0
    def addAncestro(self,ancestro):
        self.ancestro = ancestro
    def addDescendiente(self,descendiente):
        self.descendiente = descendiente
    def getName(self):
        return self.nombre
    def addPeso(self,peso):
        self.peso = peso
    def getPeso(self):
        return self.peso
    def getAncestro(self):
        return self.ancestro
    def getDescendiente(self):
        return self.descendiente


# In[3]:


class Grafo:
    
    def __init__(self, nombre):
        self.nombre = nombre

      # Función para verificar que las aristas no se repitan
    def aristaRepetida(lista, ancestro, descendiente):
        repetido = 0
        for arista in lista:
            nodo1 = arista.getAncestro()
            nodo2 = arista.getDescendiente()
            if nodo1 == ancestro: 
                  if nodo2 == descendiente:
                    repetido = 1
            if nodo2 == ancestro:
                  if nodo1 == descendiente:
                    repetido = 1
        return repetido


      #Función para guardar matriz
    def GuardarMatriz(nombre,aristas,n):
            file = open(nombre + "_" +str(n)+ ".gv", "w")
            #file = open(nombre,"w") #a para anexar al anterior texto, w para sobreescribir
            file.write("graph abstract {\n")

            for arista in aristas:
                nodo1 = arista.getAncestro().getName()
                nodo2 = arista.getDescendiente().getName()
                file.write("nodo_" + nodo1 + "->nodo_" + nodo2 + ";\n")
            file.write("}")

      #Función para guardar matriz
    def GuardarMatriz2(nombre,arbol):
            file = open(nombre + ".gv", "w")
            #file = open(nombre,"w") #a para anexar al anterior texto, w para sobreescribir
            file.write("graph abstract {\n")
            for arista in arbol:
                nodo1 = arista.getAncestro().getName()
                #print(nodo1)
                nodo2 = arista.getDescendiente().getName()
                #print(nodo2)
                file.write("nodo_" + nodo1 + "->nodo_" + nodo2 + ";\n")
            file.write("}")
            


    def GuardarMatriz2_Dijkstra(nombre,arbol):
            file = open(nombre + ".gv", "w")
            #file = open(nombre,"w") #a para anexar al anterior texto, w para sobreescribir
            file.write("graph abstract {\n")
            for arista in arbol:
                nodo1 = arista.getAncestro().getName()
                #print(nodo1)
                nodo2 = arista.getDescendiente().getName()
                #print(nodo2)
                peso = arista.getDescendiente().getPeso()
                peso2 = arista.getAncestro().getPeso()
                file.write("nodo_" + nodo1 + '('+ str(peso2) + ')' + "->nodo_" + nodo2 +'('+ str(peso) + ')' + ";\n")
            file.write("}")
            


      #Función para recontruir el arbol despues de las busquedas
    def reconstruir_arbol(nodos):
          aristas = list()
          k = 1
          for nodo in nodos:
            ancestro = nodo.getAncestro()
            if ancestro != None:
              #print(ancestro.getName())
              aristas.append(Arista(str(k)))
              arista = aristas[k-1]
              arista.addAncestro(ancestro)
              arista.addDescendiente(nodo)
              k += 1
          return aristas



      # Modelo G(m,n) de malla
    def Malla(n,m):
          nodos = list() #Creamos una lista vacía donde se guardarán todos los nodos
          aristas = list() #Creamos una lista vacía donde se guardarán todas las aristas
          #aristas.append(0)
          k = 1
          for i in range(1, m*n+1): #creamos los n nodos
            nodos.append(Nodo(str(i)))

          k = 1
          for i in range(n-1):
            for j in range(m-1):
              pos = i*m+j
              nodo = nodos[pos]
              nodo1 = nodos[pos]
              nodo2 = nodos[j+(i+1)*m]
              nodo3 = nodos[pos+1]
              aristas.append(Arista(str(k)))
              arista = aristas[k-1]
              arista.addAncestro(nodo1)
              arista.addDescendiente(nodo2)
              nodo1.addNode(nodo2)
              nodo2.addNode(nodo1)
              arista.addPeso(random.randint(1, 100))
              k += 1  
              aristas.append(Arista(str(k)))
              arista = aristas[k-1]
              arista.addAncestro(nodo1)
              arista.addDescendiente(nodo3)
              nodo3.addNode(nodo1)
              nodo1.addNode(nodo3)
              arista.addPeso(random.randint(1, 100))
              k += 1

          Grafo.GuardarMatriz("Malla",aristas,n)
          return aristas,nodos



      # Modelo Gn,m de Erdös y Rényi  
    def ErdosRenyi(n,m): # n nodos, m aristas
          nodos = list() #Creamos una lista vacía donde se guardarán todos los nodos
          aristas = list() #Creamos una lista vacía donde se guardarán todas las aristas
          for i in range(1, n+1): #creamos los n nodos
            nodos.append(Nodo(str(i)))

          #Inicia el ciclo de Erdos Renyi
          j = 1
          while j <= m and j <= n*(n-1)/2: # j menor que el número de aristas
            num1 = random.randint(0, n-1)
            num2 = random.randint(0, n-1)

            repetido = Grafo.aristaRepetida(aristas, nodos[num1],nodos[num2])

            if num1 != num2 and repetido == 0 :
              aristas.append(Arista(str(j)))
              nodo1 = nodos[num1]
              nodo2 = nodos[num2]
              nueva_arista = aristas[j-1]
              nueva_arista.addPeso(random.randint(1, 100))
              nueva_arista.addAncestro(nodo1)
              nueva_arista.addDescendiente(nodo2)
              nodo1.addNode(nodo2)
              nodo2.addNode(nodo1)
              j += 1

          Grafo.GuardarMatriz("ErdosRenyi",aristas,n)
          return aristas,nodos



      # Modelo Gn,p de Gilbert
    def Gilbert(n,p):
          nodos = list() #Creamos una lista vacía donde se guardarán todos los nodos
          aristas = list() #Creamos una lista vacía donde se guardarán todas las aristas
          for i in range(1, n+1): #creamos los n nodos
            nodos.append(Nodo(str(i)))
          k = 1
          for i in range(n):
            for j in range(n):
              prob = random.random()
              if prob < p and i != j:
                nodo1 = nodos[i]
                nodo2 = nodos[j]
                repetido = Grafo.aristaRepetida(aristas, nodos[i],nodos[j])
                if repetido == 0:
                  aristas.append(Arista(str(k)))
                  nueva_arista = aristas[k-1]
                  nueva_arista.addPeso(random.randint(1, 100))
                  nueva_arista.addAncestro(nodo1)
                  nueva_arista.addDescendiente(nodo2)
                  nodo1.addNode(nodo2)
                  nodo2.addNode(nodo1)
                  k += 1
          Grafo.GuardarMatriz("Gilbert",aristas,n)
          return aristas,nodos



      # Modelo Gn,r geográfico simple
    def Geografico(n,r):
          nodos = list() #Creamos una lista vacía donde se guardarán todos los nodos
          aristas = list() #Creamos una lista vacía donde se guardarán todas las aristas
          for i in range(1, n+1): #creamos los n nodos
            nodos.append(Nodo(str(i)))
          #Ahora debemos generar las coordenadas para cada nodo en el cuadro unitario
          x = np.random.normal(0, 0.5, n)
          y = np.random.normal(0, 0.5, n)

          k = 1
          for i in range(n):
            for j in range(i,n):
              x1 = x[i]
              x2 = x[j]
              y1 = y[i]
              y2 = y[j]
              distancia = np.sqrt((x1-x2)**2 + (y1-y2)**2)
              if distancia < r and i != j:
                nodo1 = nodos[i]
                nodo2 = nodos[j]
                repetido = Grafo.aristaRepetida(aristas, nodos[i],nodos[j])
                if repetido == 0:
                  aristas.append(Arista(str(k)))
                  nueva_arista = aristas[k-1]
                  nueva_arista.addPeso(random.randint(1, 100))
                  nueva_arista.addAncestro(nodo1)
                  nueva_arista.addDescendiente(nodo2)
                  nodo1.addNode(nodo2)
                  nodo2.addNode(nodo1)
                  k += 1
          Grafo.GuardarMatriz("Geografico",aristas,n)
          return aristas,nodos



      # Modelo Gn,d Barabási-Albert.
    def BarabasiAlbert(n,d):
          nodos = list() #Creamos una lista vacía donde se guardarán todos los nodos
          aristas = list() #Creamos una lista vacía donde se guardarán todas las aristas
          k = 1
          for i in range(1, n+1): #creamos los n nodos
            nodos.append(Nodo(str(i)))
          for i in range(n):
            nodo1 = nodos[i]
            for j in range(i):
              nodo2 = nodos[j]
              grado = nodo2.getGrado()
              p = 1 - grado/d
              #print("Nodo " + nodo2.getName() + " grado " + str(grado))

              prob = random.random()
              if p > prob:
                aristas.append(Arista(str(k)))
                arista = aristas[k-1]
                arista.addPeso(random.randint(1, 100))
                arista.addAncestro(nodo2)
                arista.addDescendiente(nodo1)
                nodo1.addNode(nodo2)
                nodo2.addNode(nodo1)
                nodo1.addGrado()
                nodo2.addGrado()
                k += 1
          Grafo.GuardarMatriz("BarabasiAlbert",aristas,n)
          return aristas,nodos


      # Modelo Gn Dorogovtsev-Mendes
    def Dorogovtsev_Mendes(n):
          nodos = list() #Creamos una lista vacía donde se guardarán todos los nodos
          aristas = list() #Creamos una lista vacía donde se guardarán todas las aristas
          for i in range(1, n+1): #creamos los n nodos
            nodos.append(Nodo(str(i)))
          nodo1 = nodos[0]
          nodo2 = nodos[1]
          nodo3 = nodos[2]
          aristas.append(Arista(str(1)))
          arista = aristas[0]
          arista.addPeso(random.randint(1, 100))
          arista.addAncestro(nodo1)
          arista.addDescendiente(nodo2)
          nodo1.addNode(nodo2)
          nodo2.addNode(nodo1)
          aristas.append(Arista(str(2)))
          arista = aristas[1]
          arista.addPeso(random.randint(1, 100))
          arista.addAncestro(nodo2)
          arista.addDescendiente(nodo3)
          nodo3.addNode(nodo2)
          nodo2.addNode(nodo3)
          aristas.append(Arista(str(3)))
          arista = aristas[2]
          arista.addPeso(random.randint(1, 100))
          arista.addAncestro(nodo3)
          arista.addDescendiente(nodo1)
          nodo3.addNode(nodo1)
          nodo1.addNode(nodo3)
          if n > 3:
            k = 4
            for i in range(3,n):
              num = random.randint(0,len(aristas)-1) #generamos un número aleatorio de arista
              arista = aristas[num]  #seleccionamos esa arista
              nodo1 = arista.getAncestro()
              nodo2 = arista.getDescendiente()
              nodo3 = nodos[i]
              aristas.append(Arista(str(k)))
              arista = aristas[k-1]
              arista.addPeso(random.randint(1, 100))
              arista.addAncestro(nodo1)
              arista.addDescendiente(nodo3)
              nodo3.addNode(nodo1)
              nodo1.addNode(nodo3)
              k += 1

              aristas.append(Arista(str(k)))
              arista = aristas[k-1]
              arista.addPeso(random.randint(1, 100))
              arista.addAncestro(nodo2)
              arista.addDescendiente(nodo3)
              nodo2.addNode(nodo3)
              nodo3.addNode(nodo2)
              k += 1
          Grafo.GuardarMatriz("Dorogovtsev-Mendes",aristas,n)
          return aristas,nodos


      # Modelo Busqueda a lo ancho
    def busquedaBFS(Grafos,lista): #grafos contiene los aristas y nodos del grafo, lista contiene el primer elemento de los nodos
          nodo_0 = lista.pop(0) #guarda el nodo inicial en nodo_0 y lo elimina de la lista
          #print("Nodo inicial " + nodo_0.getName())
          nodo_0.addRevisado() #etiqueda al nodo_0 como revisado
          nivel = nodo_0.getNivel() #marca el nivel del nodo
          conexiones = nodo_0.getConections() #obtiene las conecciones del nodo cero
          #print(conexiones)
          no_revisados = list()
          for nodo in conexiones:
            if not (nodo.getRevisado()):
              lista.append(nodo)
              no_revisados.append(nodo)
              nodo.addRevisado()
              nodo.addNivel(nivel+1)
              nodo.addAncestro(nodo_0)
          #print("Conectado con: ")
          #for nodo in no_revisados:
            #print(nodo.getName())  
          if not lista:
            aristas = Grafo.reconstruir_arbol(Grafos[1])
            return aristas 
          else:
            return Grafo.busquedaBFS(Grafos,lista)

      # Modelo Busqueda en profundidad recursivo
    def busquedaDFSr(Grafos,lista):
          nodo_0 = lista.pop(0)
          nodo_0.addRevisado()
          conexiones = nodo_0.getConections()
          for nodo in conexiones:
            if not (nodo.getRevisado()):
              lista.insert(0,nodo)
              nodo.addAncestro(nodo_0)
          if not lista: # si la lista está vacía
            aristas = Grafo.reconstruir_arbol(Grafos[1])
            return aristas 
          else:
            return Grafo.busquedaDFSr(Grafos,lista)    


      # Modelo Busqueda en profundidad interativo
    def busquedaDFSi(Grafos,nodo_0):
          lista = [nodo_0]
          while lista: #mientras la lista no esté vacía
            nodo_0 = lista.pop(0)
            nodo_0.addRevisado()
            conexiones = nodo_0.getConections()
            for nodo in conexiones:
              if not(nodo.getRevisado()):
                lista.insert(0,nodo)
                nodo.addAncestro(nodo_0)
          aristas = Grafo.reconstruir_arbol(Grafos[1])
          return aristas 
    
    
    #Función para encontrar todas las aristas que inician en nodo a (sólo para grafos dirigidos)
    def buscar_conexiones(aristas,nodo):
        lista = list()
        for arista in aristas:
            ancestro = arista.getAncestro()
            if ancestro == nodo:
                lista.append(arista)
        return lista
    
    def ordenar_prioridades(lista):
        for numPasada in range(len(lista)-1,0,-1):
            for i in range(numPasada):
                if lista[i].getPeso() > lista[i+1].getPeso():
                    temp = lista[i]
                    lista[i] = lista[i+1]
                    lista[i+1] = temp
        return lista


    def rastrear_camino(nodos,nodo_i,nodo_f):
        #print(nodo_f.getName())
        #print(len(nodos))
        for nodo in nodos:
            try:
                ancestro = nodo.getAncestro()
                #print("Nodo " + nodo.getName() + " conectado a " + ancestro.getName())
                #nodo = ancestro
            except:
                print('')
                #print(nodo.getName()+' es el nodo inicial')

    
    def Dijkstra(nodos,aristas,nodo_0,nodo_f):
        S = list()
        PQ = nodos
        i = 0
        nodo_0.addPeso(0)
        acumulado_general = nodo_0.getPeso()
        while len(PQ) > 0:
            nodo_0 = PQ[0]
            index = PQ.index(nodo_0)
            acumulado_general = nodo_0.getPeso()
            nodo = PQ.pop(index)
            S.append(nodo)
            conexiones = Grafo.buscar_conexiones(aristas,nodo_0)
            #print('Nodo_0 '+ nodo_0.getName())
            #print('Conexiones ' + str(len(conexiones)))
            for arista in conexiones:
                nodo_1 = arista.getDescendiente()
                #print('Nodo_1 '+ nodo_1.getName())
                peso = nodo_1.getPeso()
                acumulado = acumulado_general + arista.getPeso()
                #print('Acumulado '+str(acumulado))
                #print('Peso '+str(peso))
                if acumulado < peso:
                    #print(nodo_1.getName()+' '+nodo_0.getName())
                    nodo_1.addPeso(acumulado)
                    nodo_1.addAncestro(nodo)
            PQ = Grafo.ordenar_prioridades(PQ)
        camino_corto = Grafo.rastrear_camino(S,nodo_0,nodo_f)
        aristas = Grafo.reconstruir_arbol(S)
        #print('longitud '+str(len(S)))
        return aristas


# In[4]:


#código para generar grafos
Malla1 = Grafo.Malla(5,6) 
aristas,nodos = Malla1
nodos.pop(-1)
nodo_0 = nodos[0]
nodo_f = nodos[-1]
arbol = Grafo.Dijkstra(nodos,aristas,nodo_0,nodo_f)
Grafo.GuardarMatriz2_Dijkstra("Malla1",arbol)

ErdosRenyi1 = Grafo.ErdosRenyi(30,90)
aristas,nodos = ErdosRenyi1
nodo_0 = nodos[0] 
nodo_f = nodos[-1]
arbol = Grafo.Dijkstra(nodos,aristas,nodo_0,nodo_f)
Grafo.GuardarMatriz2_Dijkstra("ErdosRenyi1",arbol)

Gilbert1 = Grafo.Gilbert(30,0.4) 
aristas,nodos = Gilbert1
nodo_0 = nodos[0] 
nodo_f = nodos[-1]
arbol = Grafo.Dijkstra(nodos,aristas,nodo_0,nodo_f)
Grafo.GuardarMatriz2_Dijkstra("Gilbert1",arbol)

Geografico1 = Grafo.Geografico(30,0.5)
aristas,nodos = Geografico1
nodo_0 = nodos[0] 
nodo_f = nodos[-1]
arbol = Grafo.Dijkstra(nodos,aristas,nodo_0,nodo_f)
Grafo.GuardarMatriz2_Dijkstra("Geografico1",arbol)

BarabasiAlbert1 = Grafo.BarabasiAlbert(30,6)
aristas,nodos = BarabasiAlbert1
nodo_0 = nodos[0] 
nodo_f = nodos[-1]
arbol = Grafo.Dijkstra(nodos,aristas,nodo_0,nodo_f)
Grafo.GuardarMatriz2_Dijkstra("BarabasiAlbert1",arbol)

Dorogovtsev_Mendes1 = Grafo.Dorogovtsev_Mendes(30)
aristas,nodos = Dorogovtsev_Mendes1
nodo_0 = nodos[0] 
nodo_f = nodos[-1]
arbol = Grafo.Dijkstra(nodos,aristas,nodo_0,nodo_f)
Grafo.GuardarMatriz2_Dijkstra("Dorogovtsev_Mendes1",arbol)


# In[5]:


Malla2 = Grafo.Malla(10,10)
aristas,nodos = Malla2
nodos.pop(-1)
nodo_0 = nodos[0] 
nodo_f = nodos[-1]
arbol = Grafo.Dijkstra(nodos,aristas,nodo_0,nodo_f)
Grafo.GuardarMatriz2_Dijkstra("Malla2",arbol)

ErdosRenyi2 = Grafo.ErdosRenyi(100,700)
aristas,nodos = ErdosRenyi2
nodo_0 = nodos[0] 
nodo_f = nodos[-1]
arbol = Grafo.Dijkstra(nodos,aristas,nodo_0,nodo_f)
Grafo.GuardarMatriz2_Dijkstra("ErdosRenyi2",arbol)

Gilbert2 = Grafo.Gilbert(100,0.4)
aristas,nodos = Gilbert2
nodo_0 = nodos[0] 
nodo_f = nodos[-1]
arbol = Grafo.Dijkstra(nodos,aristas,nodo_0,nodo_f)
Grafo.GuardarMatriz2_Dijkstra("Gilbert2",arbol)

Geografico2 = Grafo.Geografico(100,0.5)
aristas,nodos = Geografico2
nodo_0 = nodos[0] 
nodo_f = nodos[-1]
arbol = Grafo.Dijkstra(nodos,aristas,nodo_0,nodo_f)
Grafo.GuardarMatriz2_Dijkstra("Geografico2",arbol)

BarabasiAlbert2 = Grafo.BarabasiAlbert(100,6)
aristas,nodos = BarabasiAlbert2
nodo_0 = nodos[0] 
nodo_f = nodos[-1]
arbol = Grafo.Dijkstra(nodos,aristas,nodo_0,nodo_f)
#print(len(arbol))
Grafo.GuardarMatriz2_Dijkstra("BarabasiAlbert2",arbol)

Dorogovtsev_Mendes2 = Grafo.Dorogovtsev_Mendes(100)
aristas,nodos = Dorogovtsev_Mendes2
nodo_0 = nodos[0] 
nodo_f = nodos[-1]
arbol = Grafo.Dijkstra(nodos,aristas,nodo_0,nodo_f)
Grafo.GuardarMatriz2_Dijkstra("Dorogovtsev_Mendes2",arbol)


# In[ ]:




