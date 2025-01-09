def solution(records):
    answer, user = {}, {}
    
    for idx in range(len(records)):
        tmp = records[idx].split()
        
        act, uid = tmp[0], tmp[1]
        
        if act == 'Leave':
            answer[uid].append([idx, act, f"{user[uid]}님이 나갔습니다."])
        else:
            nic = tmp[2]
            user[uid] = nic
            
            if uid in answer:
                tmp_ans = answer[uid]
                for idx_ans in range(len(tmp_ans)):
                    act_ans = tmp_ans[idx_ans][1]
                    tmp_ans[idx_ans][2] = f"{nic}님이 들어왔습니다." if act_ans == 'Enter' else f"{nic}님이 나갔습니다."
            else:
                answer[uid] = []
            
            if act == 'Enter':
                answer[uid].append([idx, act, f"{user[uid]}님이 들어왔습니다."])

    result = []
    for value in answer.values():
        result.extend(value)
    
    return [value[2] for value in sorted(result, key=lambda x: x[0])]