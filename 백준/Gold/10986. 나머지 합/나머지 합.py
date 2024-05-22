import sys
input = sys.stdin.readline

# 입력 받기
n, m = map(int, input().split())
array = list(map(int, input().split()))

# 누적 합 배열 및 나머지 카운트 배열
prefix_sum = 0
remainder_count = [0] * m
remainder_count[0] = 1  # 나머지가 0인 경우도 포함하기 위해 초기값 1

count = 0

for num in array:
    prefix_sum += num
    remainder = prefix_sum % m
    count += remainder_count[remainder]
    remainder_count[remainder] += 1

print(count)
