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
        obj.addEdge(a, b)

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
    def func3(self, source, target):
        # Dictionary of all weighted edges to all vertices
        cost = [[0, 351, 2853, 756, 6886],
                [351, 0, 2955, 776, 7128],
                [2853, 2955, 0, 2180, 4532],
                [756, 776, 2180, 0, 6446],
                [6886, 7128, 4532, 6446, 0]]
        # Create weighted matrix based on the graph
        for i in range(0, 5):
            for j in range(0, 5):
                if self.__g[i][j] == 1:
                    self.__Cost[i][j] = cost[i][j]
                else:
                    self.__Cost[i][j] = 0

        # Create an array of 5 elements with max integer value
        dis = [sys.maxsize] * self.__n
        # Create an array of 5 elements with -1 value
        parent = [-1] * self.__n
        # Make distance of source value to zero
        dis[source] = 0
        # Create an array of 5 elements with false boolean
        sptSet = [False] * self.__n

        k = 0
        while k < self.__n:
            # u always equals source in first iteration
            # Choose the shortest distance from the set is dist
            u = self.minDistance(dis, sptSet)
            # After u is chosen sptSet of u's index becomes true so that
            # it won't be chosen again in next iteration
            sptSet[u] = True
            for v in range(self.__n):
                if self.__Cost[u][v] > 0 and sptSet[v] == False and dis[v] > dis[u] + self.__Cost[u][v]:
                    dis[v] = dis[u] + self.__Cost[u][v]
                    parent[v] = u
            # After dijkstra algorithm finish finding all possible path
            # and still no path found to target vertex, random edges at random
            # vertices created until path exist to target vertex
            if k == 4 and dis[target] == sys.maxsize:
                k = -1
                obj.random_edge()
                cost = [[0, 351, 2853, 756, 6886],
                        [351, 0, 2955, 776, 7128],
                        [2853, 2955, 0, 2180, 4532],
                        [756, 776, 2180, 0, 6446],
                        [6886, 7128, 4532, 6446, 0]]

                for i in range(0, 5):
                    for j in range(0, 5):
                        if self.__g[i][j] == 1:
                            self.__Cost[i][j] = cost[i][j]
                        else:
                            self.__Cost[i][j] = 0

                dis = [sys.maxsize] * self.__n
                parent = [-1] * self.__n
                dis[source] = 0
                sptSet = [False] * self.__n
            k += 1
        # Prints weighted edges matrix with available edges
        print("\nWeighted Adjacency Matrix")
        for i in range(0, self.__n):
            print()
            for j in range(0, self.__n):
                print("", self.__Cost[i][j], end="")
        print()

        self.printSolution(dis, parent, source, target)
        self.drawgraph()

    def printPath(self, parent, j):
        # Prints the shortest path
        # Base Case : If j is source
        if parent[j] == -1:
            print("\t\t\t", self.__A[j], end=" "),
            return
        self.printPath(parent, parent[j])
        print("-->", self.__A[j], end=" "),

    def printSolution(self, dist, parent, source, target):
        # Prints the total distance taken
        print("\nTarget \t\tDistance from Source \t\tPath")
        print(self.__A[source], "-->", self.__A[target], "\t\t\t", dist[target], end=" "), self.printPath(parent,
                                                                                                          target)
        print()

    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        min_index = -1
        for v in range(self.__n):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        # If no smaller vertices found, then it assigns to other vertices
        # that have false in the sptSet array.
        if min_index == -1:
            for v in range(self.__n):
                if sptSet[v] == False:
                    min_index = v
        return min_index


def menu():
    print("###########     MENU       ###########")
    print(">>> Select an option from below <<<")
    print("      1) Add An Edge ")
    print("      2) Remove An Edge ")
    print("      3) Display the graph")
    print("      4) Display the adjaceny matrix")
    print("      5) Strongly connected Graph")
    print("      6) Cycle detection")
    print("      7) Shortest Path")
    print("      8) Reset the graph")
    print("      9) Exit Program")


def map_menu():
    print("\nRefer to this table to key in the number")
    print("       1) Edinburgh    4) Brussels")
    print("       2) Dublin       5) Jaipur")
    print("       3) Istanbul")


v = 5  # v is the number of vertex
obj = Graph(v)
print("\n ## The Default graph is printed out! ## \n")
obj.drawgraph()

while True:
    menu()
    val = int(input("Your option : "))
    while val > 10 or val < 1:
        print("Incorrect choosing. Please choose again")
        val = int(input())

    if val == 1:
        print(">> Add a new edge <<")
        print("\nAdd a directed edge based on the format below ")
        print("          'Vertex A' to 'Vertex B'")
        map_menu()
        dari = int(input("Vertex A : ")) - 1
        ke = int(input("Vertex B : ")) - 1
        while (dari > 5 or dari < 1) and (ke > 5 or ke < 1):
            print("Incorrect choosing. Please choose again")
            dari = int(input("Vertex A : "))
            ke = int(input("Vertex B : "))
        obj.addEdge(dari, ke)
        print(">> Succesfully added the new edge !\n")
        obj.drawgraph()

    elif val == 2:
        print(">> Remove an edge <<")
        print("\nRemove a directed edge based on the format below ")
        print("          'Vertex A' to 'Vertex B'")
        map_menu()
        dari = int(input("Vertex A : ")) - 1
        ke = int(input("Vertex B : ")) - 1
        while (dari > 5 or dari < 1) and (ke > 5 or ke < 1):
            print("Incorrect choosing. Please choose again")
            dari = int(input("Vertex A : "))
            ke = int(input("Vertex B : "))

        obj.removeEdge(dari, ke)
        print(">> Succesfully deleted the entered edge! \n ")
        obj.drawgraph()

    elif val == 3:
        print(">> Graph is displayed << \n")
        obj.drawgraph()

    elif val == 4:
        print(">> The adjaceny matrix is printed out << ")
        obj.displayAdjacencyMatrix()
        print("\n")

    elif val == 5:
        print(">> Graph connectivity << ")
        print("Choose one of the option below: ")
        print("1) Check if the current graph is strongly connected or not")
        print("2) Create a strongly connected graph")
        choice = int(input("Your option: "))
        if (choice == 1):
            if Strongly_connected(obj):
                print(">> YES, the graph is strongly connected\n")
            else:
                print(">> NO, the graph is not strongly connected\n")
        if (choice == 2):
            create_strongly_connected(obj)
            obj.drawgraph()
            print("The pathway of each vertex visiting every other vertices ")
            disp_Strongly_connected(obj)

    elif val == 6:
        print(">> Cycle detection << ")
        visited = [0] * v
        pred = [999] * v
        pred_local = [-7] * v
        lc = 1
        local_pos = 1
        for xii in range(5):
            obj.cycle_det(xii, visited, pred, lc, local_pos, pred_local)
            if (obj.hascycle == False):
                print("No cycle detected, random edges will be added now!")
                print(">>> After adding in random edges : ")
            while (obj.hascycle == False):
                obj.random_edge()
                obj.cycle_det(xii, visited, pred, lc, local_pos, pred_local)
        print("\n")
        obj.drawgraph()

    elif val == 7:
        print(">> Shortest path << ")
        print("\nChoose the vertices based on the format below ")
        print("          'Vertex A' to 'Vertex B'")
        map_menu()
        start = int(input("Vertex A : ")) - 1
        end = int(input("Vertex B : ")) - 1
        while (start > 5 or start < 1) and (end > 5 or end < 1):
            print("Incorrect choosing. Please choose again")
            start = int(input()) - 1
            end = int(input()) - 1
        obj.func3(start, end)
        print("\n")

    elif val == 8:
        print(">> The graph is RESET back to the default graph \n")
        obj.reset_graph(5)
        obj.drawgraph()

    elif val == 9:
        print("Thank you for using our app")
        sys.exit()
