from collections import deque

def solution(queue1, queue2):
    answer = 0
    
    sum_1, sum_2 = sum(queue1), sum(queue2)
    # print(sum_1, sum_2)
    if sum_1 > sum_2:
        queue1, queue2 = deque(queue1), deque(queue2)
    else:
        sum_1, sum_2 = sum_2, sum_1
        queue1, queue2 = deque(queue2), deque(queue1)
    # print(queue1, queue2)
    
    n = len(queue1)
    for _ in range(2 * (n + 2)):
        if sum_1 == sum_2: return answer
        
        if sum_1 > sum_2:
            tmp = queue1.popleft()
            queue2.append(tmp)
            sum_1 -= tmp
            sum_2 += tmp
            # print(queue1, queue2, tmp)
        else:
            tmp = queue2.popleft()
            queue1.append(tmp)
            sum_1 += tmp
            sum_2 -= tmp
        
        answer += 1
    
    return -1