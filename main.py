import sys
import networkx as nx
import matplotlib.pyplot as plt
import random




def Strongly_connected(obj):
    v = 5
    j = 0
    strong = [True] * v
    for i in range(v):
        visited = [False] * v
        obj.DFS(j, visited)
        if any(i is False for i in visited):
            strong[i] = False
        j += 1

    if any(i is False for i in strong):
        return False

    else:
        return True

def disp_Strongly_connected(obj):
    v = 5
    j = 0
    strong = [True] * v
    for i in range(v):
        visited = [False] * v
        obj.DFS_show(j, visited)
        if any(i is False for i in visited):
            strong[i] = False
        j += 1
        print()

    if any(i is False for i in strong):
        return False

    else:
        return True

def create_strongly_connected(obj):
    while not Strongly_connected(obj):
        obj.random_edge()

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

    def DFS(self, start, visited):
        visited[start] = True
        for i in range(self.__n):
            if self.__g[start][i] == 1 and (not visited[i]):
                self.DFS(i, visited)

    def DFS_show(self, start, visited):
        check = 0
        visited[start] = True
        for i in range(self.__n):
            if visited[i] == True:
                check += 1
        if check == 5:
            print(self.__A[start])
        else:
            print(self.__A[start], "->", end=' ')
        for i in range(self.__n):
            if self.__g[start][i] == 1 and (not visited[i]):
                self.DFS_show(i, visited)

    def random_edge(self):
        a = random.randint(0, 4)
        b = random.randint(0, 4)
        while a == b and b == a:
            a = random.randint(0, 4)
            b = random.randint(0, 4)
 #       obj.addEdge(a, b)

    def cycle_det(self, start_vertex, visited, pred, lc, local_pos, pred_local):
        label_count = lc
        visited[start_vertex] = label_count
        if label_count == 1:
            pred[start_vertex] = -10
            pred_local[start_vertex] = local_pos
        for i in range(self.__n):
            # 1 [to see if there is an edge or not] && 0 [indicates tht it is not visited]
            if Graph.__g[start_vertex][i] == 1 and (visited[i] == 0):
                local_pos = local_pos + 1
                pred[i] = start_vertex
                pred_local[i] = local_pos
                label_count = label_count + 1
                visited[i] = label_count
                self.cycle_det(i, visited, pred, label_count, local_pos, pred_local)
            elif Graph.__g[start_vertex][i] == 1 and (visited[i] != -1):  # check this != condition over here
                print("\nCycle detected :")
                self.hascycle = True
                self.print_cycle(visited, i)
        visited[start_vertex] = -1  # labelled as -1 when it is no longer considered, when you have backtracked

    def print_cycle(self, visited, i):
        map_list = ['Ed', 'Du', 'Is', 'Br', 'Jp']
        count = [False] * self.__n
        cycle = [-1] * self.__n
        reach = 0
        max = 0
        num = 0
        for m in range(self.__n):
            for j in range(self.__n):
                if visited[j] >= max and count[j] == False:
                    max = visited[j]
                    num = j
            if num == i:
                reach = 1
            count[num] = True
            for k in range(self.__n):
                if cycle[k] == -1:
                    cycle[k] = num
                    break
            max = -1
            if reach == 1:
                break
        for p in range(4, -1, -1):
            if cycle[p] != -1:
                print(map_list[cycle[p]], "-->", end=" ")
        for p in range(4, -1, -1):
            if cycle[p] != -1:
                print(map_list[cycle[p]])
                break
