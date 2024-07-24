from sys import stdin, stdout
input = stdin.readline
output = stdout.write

import math

A, B = map(int, input().split())
n = int(math.sqrt(B)) + 1

is_prime = [True for _ in range(n + 1)]
is_prime[0] = is_prime[1] = False
for i in range(n + 1):
    if is_prime[i]:
        for j in range(i + i, n + 1, i):
            is_prime[j] = False
is_prime = [i for i in range(2, n + 1) if is_prime[i]]

count = 0
for prime in is_prime:
    k = 2
    while True:
        almost_prime = prime ** k
        if almost_prime > B:
            break
        if almost_prime >= A:
            count += 1
        k += 1
print(count)