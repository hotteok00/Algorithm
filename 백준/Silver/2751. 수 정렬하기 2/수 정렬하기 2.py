from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N = int(input())

arr = []
for _ in range(N):
    arr.append(int(input()))

def merge_sort(s, e):
    if e - s < 1: return

    m = (s + e) // 2
    merge_sort(s, m)
    merge_sort(m + 1, e)

    tmp = []
    for i in range(s, e + 1):
        tmp.append(arr[i])

    flag = s
    idxR = s
    idxL = m + 1
    while idxR <= m and idxL <= e:
        if tmp[idxR - s] < tmp[idxL - s]: 
            arr[flag] = tmp[idxR - s]
            idxR += 1
        else:
            arr[flag] = tmp[idxL - s]
            idxL += 1
        flag += 1
    while idxR <= m:
        arr[flag] = tmp[idxR - s]
        idxR += 1
        flag += 1
    while idxL <= e:
        arr[flag] = tmp[idxL - s]
        idxL += 1
        flag += 1

merge_sort(0, N-1)

for i in range(N):
    output(str(arr[i]) + '\n')