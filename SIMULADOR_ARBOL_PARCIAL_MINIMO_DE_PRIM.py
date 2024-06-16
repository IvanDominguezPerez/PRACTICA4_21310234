#Practica4: SIMULADOR_ARBOL_PARCIAL_MINIMO_DE_PRIM
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

import networkx as nx  # Importa la biblioteca NetworkX para manejar grafos
import matplotlib.pyplot as plt  # Importa Matplotlib para la visualización gráfica
import heapq  # Importa la biblioteca heapq para manejar la cola de prioridad

def prim_mst(graph):
    start_node = list(graph.nodes())[0]  # Elige un nodo inicial arbitrario
    visited = set([start_node])  # Marca el nodo inicial como visitado
    edges = [
        (data['weight'], start_node, to)
        for to, data in graph[start_node].items()
    ]
    heapq.heapify(edges)  # Convierte la lista de aristas en una cola de prioridad
    mst = []  # Lista para almacenar las aristas del Árbol Parcial Mínimo
    total_weight = 0  # Variable para almacenar el peso total del APM

    while edges:  # Mientras haya aristas en la cola de prioridad
        weight, frm, to = heapq.heappop(edges)  # Extrae la arista de menor peso
        if to not in visited:  # Si el vértice al que conecta la arista no ha sido visitado
            visited.add(to)  # Marca el vértice como visitado
            mst.append((frm, to, weight))  # Añade la arista al APM
            total_weight += weight  # Suma el peso de la arista al peso total

            # Añade las nuevas aristas que conectan el nuevo vértice con sus vecinos no visitados
            for to_next, data in graph[to].items():
                if to_next not in visited:
                    heapq.heappush(edges, (data['weight'], to, to_next))
    
    return mst, total_weight  # Devuelve las aristas del APM y su peso total

def draw_graph(graph, mst_edges):
    pos = nx.spring_layout(graph)  # Calcula la posición de los nodos para la visualización
    plt.figure(figsize=(10, 8))  # Configura el tamaño de la figura

    # Dibuja el grafo original con los nodos y las aristas
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=15)
    labels = nx.get_edge_attributes(graph, 'weight')  # Obtiene los pesos de las aristas
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)  # Dibuja las etiquetas de los pesos

    # Crea un nuevo grafo para el APM y añade las aristas del APM
    mst_graph = nx.Graph()
    mst_graph.add_weighted_edges_from(mst_edges)
    # Dibuja las aristas del APM en rojo
    nx.draw_networkx_edges(graph, pos, edgelist=mst_graph.edges(), width=2.0, edge_color='r')
    
    plt.title("Árbol Parcial Mínimo usando el algoritmo de Prim")  # Añade un título a la figura
    plt.show()  # Muestra la figura

# Crear un grafo y añadir aristas con pesos
G = nx.Graph()
edges = [
    ('A', 'B', 1),  # Arista entre A y B con peso 1
    ('A', 'C', 4),  # Arista entre A y C con peso 4
    ('B', 'C', 2),  # Arista entre B y C con peso 2
    ('B', 'D', 5),  # Arista entre B y D con peso 5
    ('C', 'D', 3)   # Arista entre C y D con peso 3
]
G.add_weighted_edges_from(edges)  # Añade las aristas al grafo

# Encontrar el APM usando el algoritmo de Prim
mst_edges, total_weight = prim_mst(G)
print(f"Peso total del Árbol Parcial Mínimo: {total_weight}")  # Imprime el peso total del APM
print("Aristas del Árbol Parcial Mínimo:")  # Imprime las aristas del APM
for frm, to, weight in mst_edges:
    print(f"{frm} - {to}: {weight}")

# Dibujar el grafo y el APM
draw_graph(G, mst_edges)
