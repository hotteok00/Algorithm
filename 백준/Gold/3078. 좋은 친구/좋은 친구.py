N, K = map(int, input().split())
cnt = 0

from sys import stdin
names = [len(stdin.readline().rstrip()) for _ in range(N)]
switch = [0 for _ in range(21)]
for i in range(N):
    n = names[i]
    cnt += switch[n]
    switch[n] += 1
    
    if i >= K: switch[names[i - K]] -= 1

print(cnt)