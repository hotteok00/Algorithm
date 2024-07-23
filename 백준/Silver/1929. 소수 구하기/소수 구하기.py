from sys import stdin, stdout
input = stdin.readline
output = stdout.write

M, N = map(int, input().split())

eratosthenes = [True] * (N + 1)
eratosthenes[0] = False
eratosthenes[1] = False

for i in range(2, N + 1):
    if eratosthenes[i]:
        for j in range(i + i, N + 1, i):
            eratosthenes[j] = False

for i in range(M, N + 1):
    if eratosthenes[i]: output(str(i) + '\n')