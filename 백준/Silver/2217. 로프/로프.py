from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N = int(input())

lopes = []
for _ in range(N): 
    lope = int(input())
    lopes.append(lope)
    
lopes.sort(reverse=True)

max_weight = 0
for i in range(N):
    if max_weight < lopes[i] * (i + 1):
        max_weight = lopes[i] * (i + 1)

print(max_weight)