def solution(data, ext, val_ext, sort_by):
    answer = []
    
    for code, date, mx, remain in data:
        if ext == 'code' and code < val_ext:
            answer.append([code, date, mx, remain])
        elif ext == 'date' and date < val_ext:
            answer.append([code, date, mx, remain])
        elif ext == 'maximum' and mx < val_ext:
            answer.append([code, date, mx, remain])
        elif ext == 'remain' and remain < val_ext:
            answer.append([code, date, mx, remain])
    
    if sort_by == 'code':       sort_by = 0
    elif sort_by == 'date':     sort_by = 1
    elif sort_by == 'maximum':  sort_by = 2
    elif sort_by == 'remain':   sort_by = 3
    
    answer.sort(key = lambda x : x[sort_by])
    return answer