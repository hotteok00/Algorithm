from sys import stdin, stdout
input = stdin.readline
output = stdout.write

from collections import deque
import heapq

N = int(input())
cards = []
cmp_sum = 0

heapq.heapify(cards)
for _ in range(N):
    heapq.heappush(cards, int(input()))

for _ in range(N - 1):
    cmp_cnt = heapq.heappop(cards) + heapq.heappop(cards)
    heapq.heappush(cards, cmp_cnt)
    cmp_sum += cmp_cnt

print(cmp_sum)