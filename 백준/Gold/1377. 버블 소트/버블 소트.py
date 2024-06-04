from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N = int(input())
num = []

for i in range(N):
    num.append((int(input()), i))

Max = 0
sortedNum = sorted(num)

for i in range(N):
    if Max < sortedNum[i][1] - i:
        Max = sortedNum[i][1] - i

print(Max + 1)