from sys import stdin, stdout
input = stdin.readline
output = stdout.write

cnt0, cnt1 = 0, 0
S = list(map(int, list(input())[:-1]))
prev = ''
for n in S:
    if prev != n:
        prev = n
        if n == 0: cnt0 += 1
        else: cnt1 += 1

if cnt0 > cnt1: output(str(cnt1) + '\n')
else: output(str(cnt0) + '\n')