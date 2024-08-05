from sys import stdin, stdout
input = stdin.readline
output = stdout.write

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

def gcd(x, y):
    a, b = x, y
    if a < b: a, b = b, a   # a > b
    while b: a, b = b, a % b
    return a

gcd1, gcd2 = gcd(a1, b1), gcd(a2, b2)
a1, b1 = a1 // gcd1, b1 // gcd1
a2, b2 = a2 // gcd2, b2 // gcd2

# LCD = b1 * b2 / GCD(b1, b2)
lcd = b1 * b2 // gcd(b1, b2)

a1 *= lcd // b1
a2 *= lcd // b2

gcd3 = gcd(a1 + a2, lcd)

print((a1 + a2) // gcd3, lcd // gcd3)