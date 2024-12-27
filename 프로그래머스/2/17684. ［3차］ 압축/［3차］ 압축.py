def solution(msg):
    answer = []
    
    word_dict = {chr(ord('A') + i) : i + 1 for i in range(26)}
    
    s_idx = 0
    e_idx = 0
    new = 27
    while s_idx < len(msg):
        w = ''
        tmp_idx = 0
        for c in msg[s_idx:]:
            if w + c not in word_dict:
                word_dict[w + c] = new
                new += 1
                answer.append(word_dict[w])
                e_idx += tmp_idx
                break
            else:
                w += c
                tmp_idx += 1
        s_idx += len(w)
        
    answer.append(word_dict[msg[e_idx:]])
    
    return answer