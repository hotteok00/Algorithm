from collections import deque

N, L = map(int, input().split())

num = list(map(int, input().split()))
tmp = deque()

left, right = 0, 0
m = num[left]
top = m

D = []

while right < N:
    while len(tmp) > 0:
        top = tmp[-1]     
        if top <= num[right]:
            break
        else:
            tmp.pop()

    tmp.append(num[right])
    
    D.append(str(tmp[0]))
    D.append(' ')
    
    if right - left == L - 1:
        if num[left] == tmp[0]:
            tmp.popleft()
        right += 1
        left += 1
    else:
        right += 1
    
print(''.join(D))