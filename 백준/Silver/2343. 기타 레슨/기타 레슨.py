from sys import stdin, stdout
input = stdin.readline
output = stdout.write

# N, M = 강의 수, 블루레이 수
# array = 강의 길이 N개

N, M = map(int, input().split())
lectures = list(map(int, input().split()))

max_length = 0
total_sum = 0

for i in lectures:
    total_sum += i
    if max_length < i:
        max_length = i

left, right = max_length, total_sum

while left <= right:
    mid = (left + right) // 2

    tmp_sum = 0
    count = 0
    for i in lectures:
        if tmp_sum + i > mid:
            count += 1
            tmp_sum = 0
        tmp_sum += i
    
    if tmp_sum != 0: count += 1

    if count > M:
        left = mid + 1
    else:
        right = mid - 1
        
# output
# 가능한 블루레이의 최소 크기

print(left)