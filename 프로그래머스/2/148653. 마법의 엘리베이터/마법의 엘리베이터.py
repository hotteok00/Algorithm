def solution(storey):
    answer = 0
    while storey:
        tmp = storey % 10
        # print(tmp, end=' ')
        if tmp > 5:
            answer += 10 - tmp
            storey += 10 - tmp
        elif tmp < 5:
            answer += tmp
        else:
            tmp2 = storey + 5
            if tmp2 % 100 == 0 or 100 - (tmp2 % 100) < tmp2 % 100:
                storey += 5
            answer += 5
                
        storey //= 10
    return answer