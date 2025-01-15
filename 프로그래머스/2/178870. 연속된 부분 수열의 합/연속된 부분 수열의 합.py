def solution(sequence, k):
    answer = [0, len(sequence)-1]
    
    s_idx, e_idx = answer[1], answer[1]
    sub_sum = sequence[e_idx]
    
    while s_idx > -1:
        if k < sub_sum:
            sub_sum -= sequence[e_idx]
            e_idx -= 1
            if s_idx > e_idx: 
                s_idx = e_idx
                sub_sum = sequence[s_idx]
        elif k > sub_sum:
            s_idx -= 1
            sub_sum += sequence[s_idx]
        else:
            if answer[1] - answer[0] >= e_idx - s_idx:
                answer = [s_idx, e_idx]
            sub_sum -= sequence[e_idx]
            e_idx -= 1
            s_idx -= 1
            sub_sum += sequence[s_idx]
        # print(s_idx, e_idx, sub_sum)
        
    return answer