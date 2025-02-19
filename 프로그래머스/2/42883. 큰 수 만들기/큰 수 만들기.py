def solution(number, k):
    answer = []
    
    for num in number:
        while  k > 0 and answer and answer[-1] < num:
            k -= 1
            answer.pop()
        answer.append(num)
    
    if k > 0:
        answer = answer[:-k]
    
    return ''.join(answer)