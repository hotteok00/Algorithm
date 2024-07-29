from sys import stdin, stdout
input = stdin.readline
output = stdout.write

T = int(input())

Quarter = 25
Dime = 10
Nickel = 5
Penny = 1

for _ in range(T):
    C = int(input())
    q = C // Quarter
    d = (C - q * Quarter) // Dime
    n = (C - q * Quarter - d * Dime) // Nickel
    p = (C - q * Quarter - d * Dime - n * Nickel) // Penny
    output(str(q) + ' ' + str(d) + ' ' + str(n) + ' ' + str(p) + '\n')