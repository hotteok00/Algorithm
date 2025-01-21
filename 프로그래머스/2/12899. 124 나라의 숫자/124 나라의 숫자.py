def solution(n):
    answer = []
    
    elements = ['', '1', '2', '4']
    
    i = 1
    sum_of_sequence = 0
    cnt_sum = 0
    while sum_of_sequence < n:
        i *= 3
        sum_of_sequence += i
        cnt_sum += 1
        
    # print(cnt_sum, sum_of_sequence, i)
    
    current_sequence = i // 3
    while current_sequence:
        for idx in [1, 2, 3]:
            if (sum_of_sequence - i) + idx * current_sequence >= n:
                answer.append(elements[idx])
                sum_of_sequence = (sum_of_sequence - i) + idx * current_sequence
                i //= 3
                current_sequence //= 3
                break
    
    # print(answer)
    
#     answer = []
    
#     prv = 0
#     cmp = 1
#     while prv + 3 * cmp < n:
#         cmp *= 3
#         prv += cmp
    
#     while cmp:
#         tmp = min(3, n // cmp)
#         if cmp > 1 and (n - cmp * tmp) // (cmp // 3) == 0: tmp -= 1
#         answer.append(tmp)
#         n -= tmp * cmp
#         cmp //= 3
    
    for i in range(len(answer)):
        answer[i] = str(answer[i]) if answer[i] != 3 else '4'
    
    return ''.join(answer)