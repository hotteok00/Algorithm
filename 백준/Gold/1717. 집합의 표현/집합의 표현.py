from sys import stdin, stdout, setrecursionlimit
input = stdin.readline
output = stdout.write
setrecursionlimit(10 ** 5)

n, m = map(int, input().split())

elements = [i for i in range(n + 1)]

def find(a):
    if a == elements[a]:
        return a
    
    elements[a] = find(elements[a])
    return elements[a]

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        elements[a] = b

for _ in range(m):
    t, a, b = map(int, input().split())
    
    if t == 0:
        union(a, b)
    else: 
        a, b = find(a), find(b)
        if a == b:  output("YES\n")
        else:       output("NO\n")