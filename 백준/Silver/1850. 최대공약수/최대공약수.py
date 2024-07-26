from sys import stdin, stdout
input = stdin.readline
output = stdout.write

A, B = map(int, input().split())

while A:
    B, A = A, B % A

print('1' * B)