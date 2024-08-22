from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N = int(input())

node = [[0, 0] for _ in range(N + 1)]   # time, count
edge = [[] for _ in range(N + 1)]       # prev -> [next]

for i in range(1, N + 1):
    line = list(map(int, input().split()))
    node[i][0] = line[0]
    node[i][1] += len(line) - 2
    for j in line[1:-1]: edge[j].append(i)
    
from collections import deque
next_node_queue = deque()

for i in range(1, N + 1):
    if node[i][1] == 0: next_node_queue.append(i)

time = [0 for _ in range(N + 1)]
while next_node_queue:
    current_node = next_node_queue.popleft()
    time[current_node] += node[current_node][0]
    
    for next_node in edge[current_node]:
        node[next_node][1] -= 1
        
        if time[next_node] < time[current_node]:
            time[next_node] = time[current_node]
            
        if node[next_node][1] == 0: 
            next_node_queue.append(next_node)

for i in range(1, N + 1): output(str(time[i]) + "\n")