from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N = int(input())

street_trees = [int(input()) for _ in range(N)]

prev_gcd = -1
for i in range(N-1):
    diff = street_trees[i + 1] - street_trees[i]

    if prev_gcd == -1: 
        prev_gcd = diff
        continue

    if prev_gcd < diff: prev_gcd, diff = diff, prev_gcd # prev_gcd > diff
    while diff: prev_gcd, diff = diff, prev_gcd % diff

print((street_trees[-1] - street_trees[0]) // prev_gcd - 1 - (len(street_trees) - 2))