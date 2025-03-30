import pandas as pd
from collections import deque

#Establecer las rutas - DataFrame
data = {
    'Inicio': ['A', 'A', 'B', 'B', 'C', 'D', 'E', 'F'],
    'Destino': ['B', 'C', 'D', 'E', 'F', 'G', 'G', 'G']
}
rutas_df = pd.DataFrame(data)


#Funcion para determinar paradas
def obtener_paradas(rutas_df, nodo):
    return rutas_df[rutas_df['Inicio'] == nodo]['Destino'].tolist()


#Buscar la mejor ruta - busqueda en anchura BFS
def buscar_ruta(rutas_df, inicio, destino):
    #Cola para almacenar los caminos posibles
    cola = deque([[inicio]])

    #Conjunto para rastrear los nodos visitados
    visitados = set()

    while cola:
        #Extraer el primer camino de la cola
        camino = cola.popleft()

        #Obtener el ultimo nodo en el camino actual
        nodo = camino[-1]

        #Verificar si hemos llegado al destino
        if nodo == destino:
            return camino

        #Si el nodo no ha sido visitado, continuar la busqueda
        if nodo not in visitados:
            #Marcar el nodo como visitado
            visitados.add(nodo)

            #Obtener las paradas del nodo actual desde el DataFrame
            vecinos = obtener_paradas(rutas_df, nodo)
            for vecino in vecinos:
                nuevo_camino = list(camino)  #Crear un nuevo camino
                nuevo_camino.append(vecino)  #Agregarlo
                cola.append(nuevo_camino)

    #Si no se encuentra un camino al destino
    return None


#Buscan la mejor ruta entre dos puntos: A -> G
inicio = "A"
destino = "G"
ruta = buscar_ruta(rutas_df, inicio, destino)

if ruta:
    print(f"La mejor ruta desde {inicio} hasta {destino} es: {' -> '.join(ruta)}")
else:
    print(f"No se encontro una ruta desde {inicio} hasta {destino}.")
