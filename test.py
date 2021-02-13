from graph import Node, Graph

def printSearchResults(found, traversalPath, exactPath, start, end):
    print('path from {} to {} was{} found'.format(start, end, "" if found else " not"))
    if found:
        print("Traversal Path: "+traversalPath)
        print("Exact Path: "+exactPath)
    print()

def testSearchAlgorithms(graph: Graph, start, end):
    print("Breadth First Search")
    (found, traversalPath, exactPath) = graph.BFS(start, end)
    printSearchResults(found, traversalPath, exactPath, start, end)

    print("Depth First Search")
    (found, traversalPath, exactPath) = graph.DFS(start, end)
    printSearchResults(found, traversalPath, exactPath, start, end)

    print("Iterative Deepening Search")
    (found, traversalPath, exactPath) = graph.IDS(start, end)
    printSearchResults(found, traversalPath, exactPath, start, end)

    print("Uniform Cost Search")
    (found, traversalPath, exactPath, cost) = graph.UCS(start, end)
    printSearchResults(found, traversalPath, exactPath, start, end)
    print("Cost: "+str(cost))

#test graph A
graph_a = Graph()
edges = ['S3A', 'S2B', 'A5D', 'A1B', 'B3D', 'B2C', 'D1G', 'C3D', 'C4G']
for edge in edges:
	graph_a.addEdge(edge[0], edge[2], int(edge[1]))

print("\nGraph Adjecency List\n")
graph_a.printGraph()
print()

testSearchAlgorithms(graph_a, 'S', 'G')

#test graph B
graph_b = Graph()
edges = ['SA6', 'SB5', 'SC10', 'AD6', 'BD6', 'BE7', 'CE6', 'DG4', 'DC4', 'EA3', 'EG6']
for edge in edges:
	graph_b.addEdge(edge[0], edge[1], int(edge[2:]))

print("\nGraph Adjecency List\n")
graph_b.printGraph()
print()

testSearchAlgorithms(graph_b, 'S', 'G')

#Generated Graph
print("\n\nGraph Adjecency List\n")
generatedGraph = Graph()
generatedGraph.generateRandomGraph(7, 22)
generatedGraph.printGraph()
print()

testSearchAlgorithms(generatedGraph, 'A', 'E')
