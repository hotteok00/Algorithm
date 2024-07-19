from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N, K = map(int, input().split())
coins = []
count = 0

for _ in range(N):
    coins.append(int(input()))
    
for i in range(N-1, -1, -1):
    if K >= coins[i]:
        count += (K // coins[i])
        K -= coins[i] * (K // coins[i])

print(count)