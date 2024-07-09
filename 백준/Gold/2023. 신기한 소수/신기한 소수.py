from sys import stdin, stdout
input = stdin.readline
output = stdout.write

# input
# 신기한 소수의 자리 수

N = int(input())

# 신기한 소수의 왼쪽부터 1 ~ N 자리까지 모두 소수
# 따라서, 2 3 5 7 / 23 29 31 37 53 59 71 73 79 / 233 ...
# dfs로 탐색 가능할 듯

# 선택지 = 1, 3, 5, 7, 9
# 소수 판별기 (에라토스테네스의 체) 같은 걸로 매번 검사

max_num = int(pow(10, N))

import math
def is_prime_num(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0: return False
    return True

options_front = [2, 3, 5, 7]
options_rear = [1, 3, 5, 7, 9]

def dfs(tmp, depth):
    if depth == N:
        output(str(tmp) + '\n')
        return
    
    for i in options_rear:
        if is_prime_num(tmp * 10 + i):
            dfs(tmp * 10 + i, depth + 1)

for i in options_front:
    dfs(i, 1)
    
# output
# 자리 수와 일치하는 모든 신기한 소수