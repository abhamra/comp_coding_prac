from collections import deque

def dft(graph, root) -> None: #depth first traversal
    stack = deque()
    stack.append(root)
    while len(stack)>0:
        curr = stack.pop()
        for i in graph[curr]:
            stack.append(i)
        print(curr)

def dft_recursive(graph, root) -> None:
    print(root)
    for i in graph[root]:
        dft_recursive(graph, i)

def bft(graph, root) -> None: #breadth first traversal
    queue = deque()
    queue.append(root)
    while len(queue)>0:
        curr = queue.popleft()
        for i in graph[curr]:
            queue.append(i)
        print(curr)

directed_graph = {
    "a": ["b", "c"],
    "b": ["d"],
    "c": ["e"],
    "d": ["f"],
    "e": [],
    "f": []
}

#dft(directed_graph, "a")
#dft_recursive(directed_graph, "a")
#bft(directed_graph, "a")


def dfsHasPath(graph, src, dest) -> bool:
    stack = deque()
    stack.append(src)

    while len(stack)>0:
        curr = stack.pop()
        for i in graph[curr]:
            stack.append(i)
        if curr==dest:
            return True
    return False

has_path_graph = { #this graph is acyclic
    "f": ["g", "i"],
    "g": ["h"],
    "h": [],
    "i": ["g", "k"],
    "j": ["i"],
    "k": []
}

#print(dfsHasPath(has_path_graph, "f", "h"))

def undirectedHasPathDFS(graph, src, dest) -> bool:
    #need to guard against repeated nodes, use a list which adds nodes that have been visited before
    stack = deque()
    visited = set() #set has optimal time complexity for look ups and insertions, so checking if i is in visited is an O(1) operation
    stack.append(src)

    while len(stack)>0:
        curr = stack.pop()
        for i in graph[curr]:
            if i not in visited:
                visited.add(i)
                stack.append(i)
        if curr == dest:
            return True
    return False

undirected_graph = {#can be cyclic
    "i": ["j", "k"],
    "j": ["i", "k"],
    "k": ["i", "m", "l", "j"],
    "l": ["k"],
    "m": ["k"],
    "n": ["o"], #n and o are on an "island", where they are the only two nodes
    "o": ["n"]
}

#print(undirectedHasPathDFS(undirected_graph, "k", "j"))


#IMPORTANT! THIS ONE IS HARDER!!!

def connectedComponentsCountDFS(graph) -> int:
    count = 0

    keys = graph.keys()
    visited = set()

    for key in keys:
        if(explore(graph, key, visited)):
            count+=1
    
    return count

def explore(graph, curr, visited): #helper function for depth first traversals
    if curr in visited:
        return False
    visited.add(curr)
    
    for neighbor in graph[curr]:
        explore(graph, neighbor, visited)

    return True #this only runs when it has hit all of the neighbors

connected_component_graph = { #uses numbers, not letters as nodes
    "1": ["2"], #one connected component
    "2": ["1"],
    "3": [], #second connected component
    "4": ["6"], #third connected component
    "5": ["6"],
    "6": ["4", "5", "7", "8"],
    "7": ["6"],
    "8": ["6"]
}

#print(connectedComponentsCountDFS(connected_component_graph))

def largestComponent(graph) -> int:
    max = 0
    keys = graph.keys()
    visited = set()

    for key in keys:
        val = exploreSize(graph, key, visited)
        if val>max:
            max = val

    return max

def exploreSize(graph, curr, visited) -> int:

    if curr in visited: #base case
        return 0 #don't want to double count nodes
    
    visited.add(curr) #if not in visited (passes the above check), then add to visited to prevent cyclic behavior

    count = 1

    for neighbor in graph[curr]:
        count+=exploreSize(graph, neighbor, visited) #size accumulates the count of all of the connected nodes (keeps adding the 1)

    return count

largest_comp_graph = {
    0: [8, 1, 5],
    1: [0],
    2: [3, 4],
    3: [2, 4],
    4: [2, 3],
    5: [0, 8],
    8: [0, 5]
}

#print(largestComponent(largest_comp_graph))
#print(largestComponent(connected_component_graph))

def shortestPath(graph, src, dest) -> int:
    visited = set() #need to check if node was visited
    queue = deque() #use popleft!!
    queue.append([src, 0])
    visited.add(src)

    if src == dest:
        return 0

    while len(queue)>0:
        curr = queue.popleft()

        if curr[0] == dest:
            return curr[1]
        
        for neighbor in graph[curr[0]]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append([neighbor, curr[1]+1])
        

shortest_path_graph = {
    "v": ["w", "z"],
    "w": ["x", "v"],
    "x": ["y"],
    "y": ["z"], 
    "z": ["v", "y"]
}

print(shortestPath(shortest_path_graph, "w", "z"))
