class Graph:
    def __init__(self, path) :
        f = open(path, 'r')
        g = f.readlines()

        self.vertices=[]
        lineA = g[0].split()[0]
        self.vertices.append(lineA)
        for index in range(0,len(g)-1):
            if(g[index].split()[0] != lineA):
                lineA = g[index].split()[0]
                self.vertices.append(lineA)

        self.graph = [[0]*(len(self.vertices)-1) for _ in range(len(self.vertices))]
        x = -1
        for i in range(0,len(g)): 
            if(i % 28 == 0):
                x += 1
            y = i % (len(self.vertices) - 1)
            weight = int(g[i].split()[2])
            self.graph[x][y] = weight
        


class Union:
    def __init__(self, num_nodes) :
       self.index = [i for i in range(num_nodes)]

    def search(self, node) :
        while node != self.index[node]:
            node = self.index[node]
        return node

    def check_connection(self, node, node2) : 
        return self.search(node) == self.search(node2)
    
    def union(self, node, node2) : 
        node_root = self.search(node)
        node2_root = self.search(node2)
        if node_root == node2_root :
            return
        self.index[node_root] = node2_root

def kruskal_alogorithm(graph) : 
    MST = set()
    edges = set()

    for j in range(len(graph.vertices)-1) : 
        for k in range(len(graph.vertices)-1) :
            if graph.graph[j][k] != 0 and (k,j) not in edges :
                edges.add((j,k))
    complete_edges = sorted(edges, key=lambda e:graph.graph[e[0]][e[1]])
    union_find = Union(len(graph.vertices)-1)

    for e in complete_edges :
        x, y = e
        if union_find.check_connection(x,y) :
            continue
        union_find.union(x,y)
        MST.add(e)
    weight=0
    for item in MST:
        weight+=graph.graph[item[0]][item[1]]
    return MST,weight

if __name__ == "__main__" :
    source_graph = Graph("city-pairs.txt")
    MST,weight = kruskal_alogorithm(source_graph)  
    f = open("./city-pairs.txt", 'r')
    statement = f.readlines()
    f.close()

    o = open("./Kruskal-graph.txt", 'w')
    o.write("----- Shortest length -----\n")
    for item in MST:
      index = item[0]*28 + item[1]
      o.write(statement[index])

    o.write("\n\nTotal weight %d" %weight)  
    o.close()
    