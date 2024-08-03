from sys import stdin, stdout
input = stdin.readline
output = stdout.write

import math

while True:
    n = int(input())
    if n == -1: break
    
    divisors = []
    
    answer = 0
    limit = int(math.sqrt(n)) + 1
    for i in range(2, limit):
        if n % i == 0:
            divisors.append(i)
            answer += i
            if i != n // i:
               divisors.append(n // i)
               answer += n // i

    divisors.sort()
    divisors = [str(i) for i in divisors]
    
    if n - 1 == answer:
        output(f'{n} = {1} + ' + ' + '.join(divisors) + '\n')
    else:
        output(f'{n} is NOT perfect.\n')