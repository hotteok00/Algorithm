from sys import stdin, stdout
input = stdin.readline
output = stdout.write

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())

    lcd = a * b

    if a < b: a, b = b, a   # a > b
    while b: a, b = b, a % b

    output(str(lcd // a) + " " + str(a) + "\n")