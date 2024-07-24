from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N = int(input())

is_prime = [True for _ in range(10 * N + 1)]
is_prime[0] = is_prime[1] = False
for i in range(2, 10 * N + 1):
    if is_prime[i]:
        for j in range(i + i, 10 * N + 1, i):
            is_prime[j] = False
is_prime = [i for i in range(N, 10 * N + 1) if is_prime[i]]

count = 0
for prime in is_prime:
    flag = True
    tomato = list(str(prime))
    r, l = 0, len(tomato) - 1
    while r < l:
        if tomato[r] != tomato[l]:
            flag = False
            break
        r += 1
        l -= 1
    if flag: 
        print(prime)
        break