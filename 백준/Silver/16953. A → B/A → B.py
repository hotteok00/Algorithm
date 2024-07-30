from sys import stdin, stdout
input = stdin.readline
output = stdout.write

A, B = map(int, input().split())

cnt = 1
while True:
    if B % 10 == 1: B //= 10
    elif B % 2 == 0: B //= 2
    else:
        cnt = -1
        break
    
    cnt += 1
    
    if B < A:
        cnt = -1
        break
    elif B == A: break

print(cnt)