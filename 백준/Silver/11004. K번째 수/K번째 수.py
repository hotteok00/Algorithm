from sys import stdin, stdout
input = stdin.readline
output = stdout.write

N, K = map(int, input().split())
num = list(map(int, list(input().split())))

num.sort()

print(num[K-1])