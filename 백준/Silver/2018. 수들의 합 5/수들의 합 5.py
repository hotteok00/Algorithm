N = int(input())
cnt = 1

for i in range(2, N):
    mid = N // i
    
    if i % 2 == 0:
        if mid - (i//2) <= 0:
            if mid - (i//2) < 0: break
            if i * mid + (i//2) == N: cnt += 1
            break
        else:
            if      i * mid + (i//2) == N: cnt += 1
            elif    i * mid - (i//2) == N: cnt += 1
    else:
        if mid - (i//2) <= 0: break
        if i * mid == N: cnt += 1

print(cnt)