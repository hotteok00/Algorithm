from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

A.sort()

for b in B:
    left, right = 0, N-1
    mid = N // 2

    while True:
        if A[mid] < b:
            left = mid + 1
        elif A[mid] > b:
            right = mid - 1
        elif A[mid] == b:
            output(str(1) + "\n")
            break
        
        mid = (left + right) // 2
        
        if left > right:
            output(str(0) + "\n")
            break