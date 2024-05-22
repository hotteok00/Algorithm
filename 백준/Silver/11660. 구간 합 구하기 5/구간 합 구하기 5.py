from sys import stdin

N, M = map(int, stdin.readline().split())
num = [list(map(int, stdin.readline().split())) for _ in range(N)]

sum = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        sum[i][j] = sum[i - 1][j] + sum[i][j - 1] + num[i - 1][j - 1] - sum[i - 1][j - 1]
    
for i in range(M):
    x1, y1, x2, y2 = map(int, stdin.readline().split())

    print(sum[x2][y2] - sum[x1 - 1][y2] - sum[x2][y1 - 1] + sum[x1 - 1][y1 - 1])