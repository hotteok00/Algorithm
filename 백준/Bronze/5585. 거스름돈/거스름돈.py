from sys import stdin, stdout
input = stdin.readline
output = stdout.write

# from collections import deque
# import heapq

cost = 1000 -int(input())

cnt = 0
change = [500, 100, 50, 10, 5, 1]

for c in change:
    cnt += cost // c
    cost -= c * (cost // c)

print(cnt)