# 입력 받기
import sys
input = sys.stdin.readline

N = int(input())
meetings = []
for _ in range(N):
    s, e = map(int, input().split())
    meetings.append((s, e))

# 끝나는 시간을 기준으로 정렬, 끝나는 시간이 같다면 시작 시간을 기준으로 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

# 회의 배정
count = 0
end_time = 0

for s, e in meetings:
    if s >= end_time:
        end_time = e
        count += 1

print(count)
