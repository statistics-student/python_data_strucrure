def dfs(graph, start):
    visted=set()
    stack=[[start,0]]
    print(start)
    while stack:
        (v,next_node_idx)=stack[-1]
        if v not in graph or next_node_idx>=len(graph[v]):
            stack.pop()
            continue
        next_node=graph[v][next_node_idx]
        stack[-1][1]+=1
        if next_node not in visted:
            visted.add(next_node)
            print(next_node)
            stack.append([next_node,0])

graph = {1: [2, 3], 2: [4, 5], 3: [6]}
dfs(graph, 1)
