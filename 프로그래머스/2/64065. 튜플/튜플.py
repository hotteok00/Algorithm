def solution(s):
    answer = []
    for i in sorted(eval(f'[{s[1:-1]}]')):
        for j in list(i):
            if j not in answer:
                answer.append(j)
    return answer