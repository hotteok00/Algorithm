import sys
from collections import deque

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    edges = []
    
    for _ in range(m):
        u, v, w = map(int, input().split())
        edges.append((u, v, w))
    
    # 거리 및 이전 노드 초기화
    dist = [-float('inf')] * (n + 1)
    dist[1] = 0
    prev = [0] * (n + 1)
    
    # 벨만-포드 알고리즘 실행
    for i in range(n):
        for u, v, w in edges:
            if dist[u] != -float('inf') and dist[v] < dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                # n번째 라운드에서 갱신이 발생하면 양의 사이클 존재
                if i == n - 1:
                    # 양의 사이클에 속한 노드 추적
                    cycle = [False] * (n + 1)
                    cycle_nodes = deque([v])
                    cycle[v] = True
                    while cycle_nodes:
                        node = cycle_nodes.popleft()
                        for u2, v2, w2 in edges:
                            if u2 == node and not cycle[v2]:
                                cycle[v2] = True
                                cycle_nodes.append(v2)
                    # 도착점이 양의 사이클에 도달 가능하면 -1 출력
                    if cycle[n]:
                        print(-1)
                        return
    
    # 경로 복원
    path = []
    node = n
    while node != 0:
        path.append(node)
        node = prev[node]
    path.reverse()
    
    # 시작점에서 도착점으로의 경로가 존재하는지 확인
    if dist[n] == -float('inf'):
        print(-1)
    else:
        print(' '.join(map(str, path)))

if __name__ == "__main__":
    main()
