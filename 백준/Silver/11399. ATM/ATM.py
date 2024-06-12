from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N = int(input())
num = list(map(int, list(input().split())))
cnt = 0

num.sort()
for i in range(N):
    cnt += num[i]
    num.append(cnt)

print(sum(num[N:]))