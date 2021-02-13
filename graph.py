import operator, string, random

class Node: 
    def __init__(self, name: str):
        self.name = name
        self.neighbors = {}

    def addNeighbor(self, node: str, weight: int):
        self.neighbors[node] = weight

    #get the list of neighbors represented by (NodeName, weight) sorted by name
    def getNeighbors(self):
        return sorted(self.neighbors.items())

    #return list of neighbors (strings) without weight 
    def getNeighborsOnly(self):
        return sorted(self.neighbors.keys())

    #return list of neighbors (nodeName, weight) sorted by weight
    def getNeighborsByWeight(self):
        return sorted(self.neighbors.items(), key=operator.itemgetter(1))


class Graph:

    def __init__(self):
        self.vertices = {}
        self.TP = "" 

    def addNode(self, node: Node):
        self.vertices[node.name] = node

    def addEdge(self, head: str, tail: str, weight = 0):

        if head not in self.vertices:
            self.vertices[head] = Node(head)
        
        if tail not in self.vertices:
            self.vertices[tail] = Node(tail)

        self.vertices[head].addNeighbor(tail, weight)

    def printGraph(self):
        for node in self.vertices.values():
            print(node.name + ": " + str(node.getNeighbors()))

    # returns tuple: (found, traversal path, exact path)
    # found (whether the goal node was found)
    # Traversal path: order in which the nodes were visited
    # Exact path: Empty if the end node was not found 
    #frontier: queue
    def BFS(self, startNode: str, goalNode: str):

        if goalNode == startNode:
            return (True, startNode, startNode)

        frontier = [startNode]
        traversalPath = ""

        while(frontier):
            
            path = frontier.pop(0)
            currentNode = self.vertices[path[-1]]

            traversalPath += currentNode.name

            if currentNode.name == goalNode:
                return (True, traversalPath, path)

            #get the name of the neighbors of the current node
            neighbors = currentNode.getNeighborsOnly()

            for neighbor in neighbors:
                if neighbor not in list(path):
                    newPath = path + neighbor
                    frontier.append(newPath)


        return (False, traversalPath, "")


    #returns a tuple indicating if node was found, the traversal path, the exact path and the total cost
    def UCS(self, startNode: str, goalNode: str):
        if goalNode == startNode:
            return (True, startNode, startNode, 0)

        frontier = [(0, startNode)]
        traversalPath = ""
        
        while(frontier):
            (cost, path) = frontier.pop(0)
            currentNode = self.vertices[path[-1]]

            traversalPath += currentNode.name

            if currentNode.name == goalNode:
                return (True, traversalPath, path, cost)

            #get the name of the neighbors of the current node
            neighbors = currentNode.getNeighbors() 
            
            for (neighbor, edgeCost) in neighbors:
                if neighbor not in list(path):
                    newPath = path + neighbor
                    newCost = cost + edgeCost
                    
                    frontier.append((newCost, newPath))
                
            frontier.sort()   

        return (False, traversalPath, "", -1)
    
    #returns tuple: (found, traversal path, exact path)
    def DFS(self, startNode: str, goalNode: str):
        self.TP = ""

        (found, exactPath) = self.__dfs(startNode, goalNode, "")
        return (found, self.TP, exactPath)


    def __dfs(self, currentNodeName: str, goalNode: str, path: str):  
        currentNode = self.vertices[currentNodeName]
        path = path+currentNode.name
        self.TP += currentNode.name

        if currentNode.name == goalNode:
            return (True, path)

        neighbors = currentNode.getNeighborsOnly()

        for neighbor in neighbors:
            if neighbor not in list(path):
                (found, newPath) = self.__dfs(neighbor, goalNode, path)
                if found:
                    return (True, newPath)

        return (False, "")

    #returns tuple: (found, traversal path, exact path)
    def IDS(self, startNode: str, goalNode: str):
        self.TP = ""
        found = False
        reachedLimit = False
        limit = 0
        while(not found and not reachedLimit):
            (found, exactPath, reachedLimit) = self.__ids(startNode, goalNode, "", limit, 0)
            limit += 1
            self.TP += " "
        
        
        return (found, self.TP, exactPath)

    def __ids(self, currentNodeName: str, goalNode: str, path: str, limit: int, i: int):

        currentNode = self.vertices[currentNodeName]
        path += currentNode.name

        reachedLimit = not currentNode.getNeighbors()

        if i > limit:
            return (False, "", reachedLimit)

        self.TP += currentNode.name

        if currentNode.name == goalNode:
            return (True, path, False)

        neighbors = currentNode.getNeighborsOnly()

        reachedLimit = True
        for neighbor in neighbors:
            if neighbor not in list(path):
                (found, newPath, gotToLimit) = self.__ids(neighbor, goalNode, path, limit, i+1)
                if found:
                    return (True, newPath, False)
                reachedLimit = reachedLimit and gotToLimit
        return (False, "", reachedLimit)

    
    def generateRandomGraph(self, nodes :int, edges: int):
        if not self.vertices and nodes <= 26 and nodes > 0 and edges >= 0 and edges <= nodes * (nodes - 1) :
            for i in range(0, nodes):
                name = string.ascii_uppercase[i]
                self.addNode(Node(name))

            j = 0
            while(j < edges):
                start = string.ascii_uppercase[random.randint(0, nodes-1)]
                end = string.ascii_uppercase[random.randint(0, nodes-1)]
                if start == end:
                    continue

                if end in self.vertices[start].getNeighborsOnly():
                    continue

                weight = random.randint(0, 256)

                self.vertices[start].addNeighbor(end, weight)
                j += 1

        else:
            print("something went wrong. Nodes must be <= 26, edges <= nodes*(nodes-1) and vertices dictionary should be empty already.")


