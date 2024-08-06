from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N = int(input())

is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, N + 1):
    if is_prime[i]:
        for j in range(i + i, N + 1, i):
            is_prime[j] = False
            
is_prime = [i for i in range(2, N + 1) if is_prime[i]]
# print(is_prime)

count = 0
sumOfPrimes = 0
r, l = 0, 0
while True:
    # print(sumOfPrimes, r, l)
    
    if sumOfPrimes < N:
        if l > len(is_prime) - 1: break
        sumOfPrimes += is_prime[l]
        l += 1
        continue
    
    if sumOfPrimes > N:
        if r > len(is_prime) - 1: break
        sumOfPrimes -= is_prime[r]
        r += 1
        continue
    
    if sumOfPrimes == N:
        count += 1
        if l > len(is_prime) - 1 or r > len(is_prime) - 1: break
        sumOfPrimes = sumOfPrimes + is_prime[l] - is_prime[r]
        l += 1
        r += 1
        
print(count)