from sys import stdin, stdout
input = stdin.readline
output = stdout.write

num = list(map(int, list(input().rstrip())))

for i in range(len(num)):
    for j in range(i, len(num)):
        if num[i] < num[j]:
            tmp = num[i]
            num[i] = num[j]
            num[j] = tmp

print(''.join(map(str, num)))