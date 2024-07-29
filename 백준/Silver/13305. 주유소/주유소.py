from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N = int(input()) # num of city

distance = list(map(int, input().split()))
gasStation = list(map(int, input().split()[:-1]))
subMinCost = [float('inf')] * (N - 1)

for i in range(N-1, -1, -1):
    for j in range(i, N-1):
        if subMinCost[j] > gasStation[i] * distance[j]:
            subMinCost[j] = gasStation[i] * distance[j]
    # print(distance, gasStation, subMinCost)

print(sum(subMinCost))