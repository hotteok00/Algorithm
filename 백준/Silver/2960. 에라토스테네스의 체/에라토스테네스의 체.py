from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N, K = map(int, input().split())

is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False
for i in range(2, N + 1):
    if is_prime[i]:
        for j in range(i, N + 1, i):
            if is_prime[j]:
                is_prime[j] = False
                K -= 1

            if K == 0: 
                print(j)
                break

    if K == 0: break            
