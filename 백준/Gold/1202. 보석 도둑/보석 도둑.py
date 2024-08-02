from sys import stdin, stdout
input = stdin.readline
output = stdout.write

import heapq

N, K = map(int, input().split())

jewels = []
bags = []
for _ in range(N): heapq.heappush(jewels, list(map(int, input().split())))
for _ in range(K): bags.append(int(input()))

bags.sort()
    
valueSum = 0
values = []
for bag in bags:
    while jewels and bag >= jewels[0][0]:
        w, v = heapq.heappop(jewels)
        heapq.heappush(values, -v)
        
    if values: 
        v = heapq.heappop(values)
        valueSum -= v
    elif not jewels: break
    
print(valueSum)