from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N = int(input())
local_government_budgets = list(map(int, input().split()))
total_budgets = int(input())

local_government_budgets.sort()
if total_budgets >= sum(local_government_budgets):
    print(local_government_budgets[-1])
else:
    i = 0
    while i < N and local_government_budgets[i] <= total_budgets // (N - i):
        average_budgets = total_budgets // (N - i)
        while local_government_budgets[i] <= average_budgets:
            total_budgets -= local_government_budgets[i]
            i += 1
    print(total_budgets // (N - i))