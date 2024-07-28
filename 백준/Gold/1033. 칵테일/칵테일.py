from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N = int(input())

materail_ratio = [[-1 for _ in range(N)] for _ in range(N)]
additional_prime_factors = [1] * N

for _ in range(N - 1):
    a, b, p, q = map(int, input().split())
    
    c, d = p, q
    if c < d: c, d = d, c   # c > d
    
    while d: c, d = d, c % d
    p, q = p // c, q // c
    
    materail_ratio[a][b] = p
    materail_ratio[b][a] = q

# for i in materail_ratio: print(" ".join(f"{num:2}" for num in i))
    
for i in range(N):
    stack = []
    for j in range(N):
        if materail_ratio[i][j] != -1:
            stack.append((materail_ratio[i][j], i, j))
            
            while stack:
                n, x, y = stack.pop()
                for k in range(N):
                    if k == y: continue
                    if materail_ratio[x][k] != -1:
                        additional_prime_factors[k] *= n
                        stack.append((n, k, x))
                
for i in range(N):
    for j in materail_ratio[i]:
        if j != -1: additional_prime_factors[i] *= j

# print(additional_prime_factors)

gcd = additional_prime_factors[0]
for i in range(1, N):
    a, b = gcd, additional_prime_factors[i]
    if a < b: a, b = b, a   # a > b    
    while b: a, b = b, a % b
    gcd = a

for i in additional_prime_factors:
    output(str(i // gcd) + " ")
print()