from sys import stdin, stdout
input = stdin.readline
output = stdout.write

# 1 ≤ E ≤ 15 = 1, 3, 5, 15
# 1 ≤ S ≤ 28 = 1, 2, 4, 7, 14, 28
# 1 ≤ M ≤ 19 = 1, 19

E, S, M = map(int, input().split())

# x_year = ?

# (x_year - E) % 15 == 0
# (x_year - S) % 28 == 0
# (x_year - M) % 19 == 0

s = 0
while True:
    x = 28 * s + S
    if (x - E) % 15 == 0 and (x - M) % 19 == 0:
        break
    s += 1
    
print(28 * s + S)