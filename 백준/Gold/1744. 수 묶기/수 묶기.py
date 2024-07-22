from sys import stdin, stdout
input = stdin.readline
output = stdout.write

from collections import deque
import heapq

N = int(input())

# sequence = []
# heapq.heapify(sequence)
# for _ in range(N): heapq.heappush(sequence, int(input()))

sequence_p = []
sequence_n = []
for _ in range(N): 
    i = int(input())
    if i > 0: sequence_p.append(i)
    else: sequence_n.append(i)

sequence_p.sort()
sequence_n.sort(key = lambda x: abs(x))
sequence = sequence_n + sequence_p

sum = 0
idx = N - 1
while idx > 0:
    if sequence[idx - 1] + sequence[idx] <= sequence[idx - 1] * sequence[idx]:
        sum += sequence[idx - 1] * sequence[idx]
        idx -= 2
    else:
        sum += sequence[idx]
        idx -= 1

if idx == 0:
    sum += sequence[idx]

print(sum)