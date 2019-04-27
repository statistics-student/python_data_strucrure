from queue import Queue

def bfs(graph,node):
    visted=set()
    visted.add(node)
    q=Queue()
    q.put(node)
    while not q.empty():
        u=q.get()
        print(u)
        for v in graph.get(u):
            if v not in visted:
                visted.add(v)
                q.put(v)


graph = {1: [2,3], 2: [1, 4,5], 3: [1,6], 4: [2],5:[2],6:[3]}
bfs(graph, 2)


