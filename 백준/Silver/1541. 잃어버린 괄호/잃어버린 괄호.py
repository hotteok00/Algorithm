from sys import stdin, stdout
input = stdin.readline
output = stdout.write

from collections import deque
import heapq


# input
# 수식

fomula = list(input())
numbers = deque()
operations = deque()

number = ''
for i in fomula:
    if i == '\n':
        numbers.append(int(number))
        break

    if i != '+' and i != '-':
        number += i
    else:
        numbers.append(int(number))
        number = ''
        operations.append(i)

# print(fomula, numbers, operations)

# 수식에 연산 순서 변경해서 최솟값 계산하기
# - 나오면 뒤에 - 전까지 괄호 해서 계산

sum = numbers.popleft()
i = 0
while operations:
    o = operations.popleft()
    
    # o == '-'이면 다음 '-' 또는 끝까지 괄호 계산
    if o == '-':
        tmp = numbers.popleft()
        while operations:
            o = operations.popleft()
            if o == '-':
                operations.appendleft(o)
                break
            else:
                n = numbers.popleft()
                tmp += n
        sum -= tmp

    # o == '+'이면 그냥 덧셈
    else:
        sum += numbers.popleft()
    
# output
# 연산의 순서를 적당히 바꿔서 계산한 최솟값 출력
print(sum)
