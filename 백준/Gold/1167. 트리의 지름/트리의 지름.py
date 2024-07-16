from sys import stdin
from collections import deque

input = stdin.readline

# 입력 받기
V = int(input().strip())
graph = {i: [] for i in range(1, V + 1)}

for _ in range(1, V + 1):
    arr = list(map(int, input().split()))
    u = arr[0]
    tmp = arr[1:-1]
    for j in range(0, len(tmp), 2):
        graph[u].append((tmp[j], tmp[j + 1]))

def bfs(start):
    visited = [-1] * (V + 1)
    queue = deque([start])
    visited[start] = 0
    furthest_node = start
    max_distance = 0

    while queue:
        node = queue.popleft()
        current_distance = visited[node]
        for neighbor, weight in graph[node]:
            if visited[neighbor] == -1:
                visited[neighbor] = current_distance + weight
                queue.append(neighbor)
                if visited[neighbor] > max_distance:
                    max_distance = visited[neighbor]
                    furthest_node = neighbor

    return furthest_node, max_distance

# 첫 번째 BFS: 임의의 노드 (1번 노드)에서 가장 먼 노드를 찾기
furthest_node, _ = bfs(1)

# 두 번째 BFS: 첫 번째 BFS에서 찾은 가장 먼 노드에서 가장 먼 노드를 찾기
_, max_distance = bfs(furthest_node)

# 트리의 지름 출력
print(max_distance)
