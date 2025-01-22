from collections import deque

MAX = float('inf')

def solution(N, road, K):
    answer = 0
    
    next_villages = deque()
    # visited = [False for _ in range(N+1)]
    map_of_village = [[0 for _ in range(N+1)] for _ in range(N+1)]
    distance = [MAX for _ in range(N+1)]
    
    for s, e, t in road: 
        # map_of_village[s][e] = t
        # map_of_village[e][s] = t
        if map_of_village[s][e] == 0:
            map_of_village[s][e] = t
            map_of_village[e][s] = t
        else:
            map_of_village[s][e] = min(t, map_of_village[s][e])
            map_of_village[e][s] = min(t, map_of_village[s][e])
    
    distance[1] = 0
    
    next_villages.append(1)
    # visited[1] = True
    
    while next_villages:
        nxt = next_villages.popleft()
        
        for idx in range(1, N+1):
            # if map_of_village[nxt][idx] != 0 and not visited[nxt]:
            if map_of_village[nxt][idx] != 0:
                if distance[nxt] + map_of_village[nxt][idx] < distance[idx]:
                    distance[idx] = distance[nxt] + map_of_village[nxt][idx]
                    next_villages.append(idx)

    # print(distance)
    return len([d for d in distance if d <= K])