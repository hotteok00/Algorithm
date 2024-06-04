from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N = int(input())
num = []

for _ in range(N):
    num.append(int(input()))

for i in range(N):
    for j in range(1, N):
        if num[j-1] > num[j]:
            tmp = num[j-1]
            num[j-1] = num[j]
            num[j] = tmp

for i in range(N):
    print(num[i])