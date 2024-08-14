from collections import deque

def bfs():
    queue = deque()
    queue.append((0, 0, C))
    visited[0][0][C] = True
    results = set()

    while queue:
        a, b, c = queue.popleft()

        if a == 0:
            results.add(c)
        
        # A -> B
        if a + b > B:
            new_a, new_b = a - (B - b), B
        else:
            new_a, new_b = 0, a + b
        if not visited[new_a][new_b][c]:
            visited[new_a][new_b][c] = True
            queue.append((new_a, new_b, c))
        
        # A -> C
        if a + c > C:
            new_a, new_c = a - (C - c), C
        else:
            new_a, new_c = 0, a + c
        if not visited[new_a][b][new_c]:
            visited[new_a][b][new_c] = True
            queue.append((new_a, b, new_c))
        
        # B -> A
        if b + a > A:
            new_b, new_a = b - (A - a), A
        else:
            new_b, new_a = 0, b + a
        if not visited[new_a][new_b][c]:
            visited[new_a][new_b][c] = True
            queue.append((new_a, new_b, c))
        
        # B -> C
        if b + c > C:
            new_b, new_c = b - (C - c), C
        else:
            new_b, new_c = 0, b + c
        if not visited[a][new_b][new_c]:
            visited[a][new_b][new_c] = True
            queue.append((a, new_b, new_c))
        
        # C -> A
        if c + a > A:
            new_c, new_a = c - (A - a), A
        else:
            new_c, new_a = 0, c + a
        if not visited[new_a][b][new_c]:
            visited[new_a][b][new_c] = True
            queue.append((new_a, b, new_c))
        
        # C -> B
        if c + b > B:
            new_c, new_b = c - (B - b), B
        else:
            new_c, new_b = 0, c + b
        if not visited[a][new_b][new_c]:
            visited[a][new_b][new_c] = True
            queue.append((a, new_b, new_c))

    return sorted(results)

# 입력 받기
A, B, C = map(int, input().split())

# 방문 여부를 저장하는 3차원 배열
visited = [[[False] * (C + 1) for _ in range(B + 1)] for _ in range(A + 1)]

# BFS 탐색 및 결과 출력
result = bfs()
print(' '.join(map(str, result)))