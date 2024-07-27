from sys import stdin, stdout
from collections import defaultdict

input = stdin.readline
print = stdout.write

n, k = map(int, input().split())
houses = []
for i in range(n):
    s, e = map(int, input().split())
    houses.append((s, e, i))

# Create a list of available houses for each day
available = defaultdict(list)
for s, e, i in houses:
    for day in range(s, e + 1):
        available[day].append((e, i))  # Store end day and house index

visited = [False] * n
schedule = [0] * n

# Schedule visits
for day in range(1, 32):
    if not available[day]:
        continue
    
    # Sort houses available today by end date
    available[day].sort()
    
    visits = 0
    for _, i in available[day]:
        if not visited[i] and visits < k:
            schedule[i] = day
            visited[i] = True
            visits += 1
        
        if visits == k:
            break

# Check if all houses were visited
if all(visited):
    for day in schedule:
        print(f"{day}\n")
else:
    print("No solution exists\n")