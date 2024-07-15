from sys import stdin, stdout
input = stdin.readline
output = stdout.write

# input 
# N, M = 사람 수, 친구 관계 수
# a와 b는 친구

N, M = map(int, input().split())
flag = False
visited = [False for _ in range(N)]
buddy = {i : [] for i in range(N)}
for _ in range(M):
    a, b = map(int, input().split())
    buddy[a].append(b)
    buddy[b].append(a)

# A, B > B, C > C, D > D, E => depth == 5
# depth 5 이상 갈 수 있는지 찾아보라는 뜻

def dfs(v, visited, depth):
    global flag

    if depth == 5 or flag:
        flag = True
        return
    
    for u in buddy[v]:
        if not visited[u]:
            visited[u] = True
            dfs(u, visited, depth + 1)
            visited[u] = False

for i in range(N):
    if not visited[i]:
        visited[i] = True
        dfs(i, visited, 1)
        visited[i] = False

# output
# depth >= 5 이면 1, 아니면 0

print(1 if flag else 0)