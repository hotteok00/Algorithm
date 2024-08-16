from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N = int(input())
M = int(input())

cities = [i for i in range(N + 1)]

def find(a):
    if a == cities[a]: return a
    cities[a] = find(cities[a])
    return cities[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b: cities[a] = b

for i in range(N):
    idx = i + 1
    representative = cities[idx]
    connections = [0] + list(map(int, input().split()))
    for j in range(1, N + 1):
        if connections[j] == 0: continue
        # union
        # if cities[j] == j:
        #     cities[j] = representative
        # else:
        #     if cities[representative] < cities[j]: cities[j] = cities[representative]
        #     else: cities[representative] = cities[j]
        union(idx, j)
    # print(cities)
        
travel = list(map(int, input().split()))

answer = "YES"
prev_city = travel[0]
for i in range(1, M):
    next_city = travel[i]
    
    # if cities[prev_city] != cities[next_city]:
    #     answer = "NO"
    #     break
    
    a = find(prev_city)
    b = find(next_city)
    if a != b:
        answer = "NO"
        break
    
    prev_city = next_city

print(answer)