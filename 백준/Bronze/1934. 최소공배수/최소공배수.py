from sys import stdin, stdout
input = stdin.readline
output = stdout.write

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    
    if A > B: A, B = B, A
    
    M = A * B
    while A:
        B, A = A, B % A
    
    output(str(int(M / B)) + '\n')