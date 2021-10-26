import sys
import networkx as nx
import matplotlib.pyplot as plt
import random

class Graph:
    __A = ['Ed', 'Du', 'Is', 'Br', 'Jp']
    __n = 0
    __g = [[0 for x in range(5)] for y in range(5)]
    hascycle = False # for cycle detection
    # Matrix for calculate the weight
    __Cost = [[0 for a in range(5)] for b in range(5)]

    def __init__(self, vertices):
        self.__n = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        # initializing each element of the adjacency matrix to zero
        for i in range(0, self.__n):
            for j in range(0, self.__n):
                self.__g[i][j] = 0
        self.addEdge(0, 4)
        self.addEdge(4, 3)
        self.addEdge(1, 3)
        self.addEdge(2, 1)
        self.addEdge(2, 0)
        self.hascycle = False

    def displayAdjacencyMatrix(self):
        print("Adjacency Matrix:", end="")
        # displaying the 2D array
        for i in range(0, self.__n):
            print()
            for j in range(0, self.__n):
                print("", self.__g[i][j], end="")
        print()

    def addEdge(self, x, y):
        # checks if the vertex is connecting to itself
        if x == y:
            print("Self connecting loops cannot be added!")
        else:
            # creating directed edge
            self.__g[x][y] = 1

    def removeEdge(self, x, y):
        # checks if the vertex is connecting to itself
        if x == y:
            print("Same Vertex!")
        else:
            # remove directed edge
            self.__g[x][y] = 0

    def drawgraph(self):
        G = nx.DiGraph()

        for i in range(0, self.__n):
            for j in range(0, self.__n):
                if j == i:
                    continue
                if self.__g[i][j] == 1:
                    G.add_edges_from([(self.__A[i], self.__A[j])])

        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, node_size=500)
        nx.draw_networkx_edges(G, pos, connectionstyle="arc3,rad=0.2", edgelist=G.edges(), edge_color='black')
        nx.draw_networkx_labels(G, pos)
        plt.show()

    def reset_graph(self, x):
        self.__init__(x)
