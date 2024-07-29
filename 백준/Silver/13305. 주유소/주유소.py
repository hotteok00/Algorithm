from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N = int(input()) # num of city

distance = list(map(int, input().split()))
gasStation = list(map(int, input().split()[:-1]))
subMinCost = [float('inf')] * (N - 1)

total = 0
minGasCost = float('inf')
for i in range(N - 1):
    if minGasCost > gasStation[i]: minGasCost = gasStation[i]
    total += minGasCost * distance[i]

print(total)