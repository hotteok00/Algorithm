from sys import stdin, stdout, setrecursionlimit
input = stdin.readline
output = stdout.write

setrecursionlimit(10 ** 6)

def dfs(node, color, visited):
    global ans

    for next_node in graph[node]:
        if not visited[next_node][0]:
            visited[next_node][0], visited[next_node][1] = True, not visited[node][1]
            dfs(next_node, not color, visited)
        elif visited[node][1] == visited[next_node][1]:
            ans = "NO"
        
        if ans == "NO": break

K = int(input())

for _ in range(K):
    V, E = map(int, input().split())
    
    graph = [[] for _ in range(V + 1)]

    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    ans = "YES"
    color = True
    visited = [[False, ''] for _ in range(V + 1)]
    for i in range(1, V + 1):
        if ans == "NO": break
        
        visited[i][0], visited[i][1] = True, color if visited[i][1] == '' else visited[i][1]
        dfs(i, not color, visited)

    print(ans)

