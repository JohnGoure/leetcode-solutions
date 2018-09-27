class Vertex:
    label = ''
    wasVisited = False

    def __init__ (self, label):
        self.label = label


# Adjacentcy Matrix
matrix = [[False, False, False, False]for i in range(4)]

''' To add a vertx to a graph, make a new vertex object and 
append it into your vertex list.'''
vertexList = []
vertex = Vertex('A')
vertexList.append(vertex)

class Graph:
    def __init__(self, size):
        self.vertexList = []
        self.adjMat = [[False for x in range(size)] for i in range(size)]

    def addVertex(self, label):
        self.vertexList.append(Vertex(label))

    def addEdge(self, start, end):
        self.adjMat[start][end] = True
        self.adjMat[end][start] = True

    def displayVertex(self, v):
        if v > len(self.vertexList) - 1:
            print('No vertex at positon %d.' % v)
        else:
            print(self.vertexList[v].label)

graph = Graph(5)

graph.addVertex('A')
graph.addEdge(0,1)
graph.displayVertex(0)