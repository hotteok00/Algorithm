from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N = int(input())
M = int(input())

# count
# node = [0 for _ in range(N + 1)]

# prev -> next = time, visite
# edge            = [[] for _ in range(N + 1)]
reversed_edge   = [[] for _ in range(N + 1)]
# edge = {i : [] for i in range(1, N + 1)}
# reversed_edge = {i : [] for i in range(1, N + 1)}

threshold_path = [0 for _ in range(N + 1)]

for _ in range(M):
    s, e, t = map(int, input().split())
    reversed_edge[e].append([s, t, False])
    threshold_path[e] = max(threshold_path[e], threshold_path[s] + t)
    
S, E = map(int, input().split())

from collections import deque

next_node_queue = deque()

# sort
# next_node_queue.append(S)

# while next_node_queue:
#     next_node = next_node_queue.popleft()
#     for e, t in edge[next_node]:
#         node[e] -= 1
#         threshold_path[e] = max(threshold_path[e], threshold_path[next_node] + t)
#         if node[e] == 0: next_node_queue.append(e)

# next_node_queue.clear()

# reversed sort
next_node_queue.append(E)
count = 0

while next_node_queue:
    next_node = next_node_queue.popleft()
    tmp_edge = reversed_edge[next_node]
    
    for i in range(len(tmp_edge)):
        s, t, is_visited = tmp_edge[i]
        
        if threshold_path[next_node] == threshold_path[s] + t:
            
            if not is_visited:
                
                count += 1
                tmp_edge[i][2] = True
                next_node_queue.append(s)
           
print(threshold_path[E])
print(count)