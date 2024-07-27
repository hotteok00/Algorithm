from sys import stdin, stdout
input = stdin.readline
output = stdout.write

n, k = map(int, input().split())
vacations = []
for i in range(n):
    s, e = map(int, input().split())
    vacations.append([i, s, e])
    
vacations.sort(key=lambda x: (x[2],x[1]))

visit_schedule = [0] * n
day_count = [0] * 32
for idx, s, e in vacations:
    for day in range(s, e + 1):
        if day_count[day] < k:
            day_count[day] += 1
            visit_schedule[idx] = day
            break

for v in visit_schedule:
    output(str(v) + '\n')