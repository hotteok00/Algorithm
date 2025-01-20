from collections import deque

def solution(n, wires):
    answer = []
    
    graph = {i:[] for i in range(1, n+1)}
    for s, e in wires:
        graph[s].append(e)
        graph[e].append(s)
        
    for s, e in wires:
        group_A = count_nodes(n, graph, s, e)
        group_B = count_nodes(n, graph, e, s)
    
        answer.append(abs(group_A - group_B))
    
    return sorted(answer)[0]

def count_nodes(n, graph, s, skip):
    q = deque()
    visited = [False for _ in range(n+1)]
    visited[s] = True
    
    for e in graph[s]:
        if e != skip: q.append(e)
        visited[e] = True
    
    while q:
        crt = q.popleft()
        
        for nxt in graph[crt]:
            if not visited[nxt]:
                q.append(nxt)
                visited[nxt] = True
    
    return visited.count(True)