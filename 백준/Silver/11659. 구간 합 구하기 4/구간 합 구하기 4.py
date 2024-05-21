from sys import stdin

N, M = map(int, stdin.readline().split())

num = list(map(int, stdin.readline().split()))
sum = [0]

for i in num:
  sum.append(i + sum[-1])

for _ in range(M):
  i, j = map(int, stdin.readline().split())
  print(sum[j] - sum[i - 1])