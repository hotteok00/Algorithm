from sys import stdin, stdout
input = stdin.readline
output = stdout.write

Connected_Component = 0

N, M = map(int, input().split())

visited = [False for _ in range(N + 1)]
nodes = {i:[] for i in range(N + 1)} 
for _ in range(M):
    u, v = map(int, input().split())
    nodes[u].append(v)
    nodes[v].append(u)

stack = []
for i in range(1, N + 1):
    if not visited[i]:
        Connected_Component += 1
        stack.append(i)
        
        while stack:
            u = stack.pop()

            for v in nodes[u]:
                if not visited[v]:
                    stack.append(v)
                    visited[v] = True

print(Connected_Component)