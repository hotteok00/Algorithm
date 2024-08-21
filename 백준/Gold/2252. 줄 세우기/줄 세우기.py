from sys import stdin, stdout
input = stdin.readline
output = stdout.write

from collections import deque

N, M = map(int, input().split())

edge = [[] for _ in range(N + 1)]
node = [0 for _ in range(N + 1)]

for _ in range(M): 
    a, b = map(int, input().split())
    edge[a].append(b)
    node[b] += 1
    

next_node_queue = deque()

for i in range(1, N + 1):
    if node[i] == 0:
        next_node_queue.append(i)
        
while next_node_queue:
    current_node = next_node_queue.popleft()
    output(str(current_node) + " ")
    for nn in edge[current_node]:
        node[nn] -= 1
        if node[nn] == 0: next_node_queue.append(nn)