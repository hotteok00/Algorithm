from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N = int(input())

i = 1
while N > 0:
    # print(N, i)
    N -= i
    i += 1

if N < 0: print(i - 2)
else: print(i - 1)