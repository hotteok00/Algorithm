from sys import stdin, stdout
input = stdin.readline

uniqueNums = list(map(int, input().split()))
validation = 0
for i in uniqueNums:
    validation += i * i
print(validation % 10)