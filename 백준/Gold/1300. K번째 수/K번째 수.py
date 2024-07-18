from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N = int(input())
k = int(input())

left = 1
right = k
ans = 0

while left <= right:
    mid = (left + right) // 2

    cnt = 0
    for i in range(1, N + 1):
        cnt += min(mid//i, N)
    
    if cnt < k:
        left = mid + 1
    else:
        ans = mid
        right = mid - 1

print(ans)