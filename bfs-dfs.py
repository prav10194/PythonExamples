graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start):
    visited, stack = set(), [start]
    orderedVertex=[]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            orderedVertex.append(vertex)
            stack.extend(graph[vertex] - visited)
    return orderedVertex
    
def bfs(graph,start):
    visited=set()
    queue=[start]
    orderedVertex=[]
    while queue:
        vertex=queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            orderedVertex.append(vertex)
            queue.extend(graph[vertex]-visited)
    #print(visited)
    return orderedVertex
    
print(dfs(graph,'A'))
print(bfs(graph,'A'))
