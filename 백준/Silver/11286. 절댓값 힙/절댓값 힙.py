from sys import stdin, stdout
input = stdin.readline
output = stdout.write

from queue import PriorityQueue

N = int(input())
Q = PriorityQueue()

for i in range(N):
    num = int(input())

    if num != 0:
        Q.put((abs(num), num))
    else:
        if Q.empty():
            output('0\n')
        else:
            tmp = Q.get()
            output(str((tmp[1])) + '\n')