from sys import stdin, stdout
input = stdin.readline
output = stdout.write

T = int(input())

A = 300
B = 60
C = 10

a = T // A
b = (T - a * A) // B
c = (T - a * A - b * B) // C

if T - a * A - b * B - c * C != 0: print(-1)
else: print(a, b, c)