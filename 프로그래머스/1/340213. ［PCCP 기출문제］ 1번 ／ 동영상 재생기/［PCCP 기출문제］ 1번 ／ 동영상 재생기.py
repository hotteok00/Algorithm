def solution(video_len, pos, op_start, op_end, commands):
    current = op_skip(pos, op_start, op_end)
    order = {"prev": prv, "next": nxt}
    
    for command in commands:
        current = order[command](current)
        current = time_mx(current, video_len)
        current = op_skip(current, op_start, op_end)
    
    return current

def prv(current):
    current = time_dec(current) - 10
    if current < 0: current = 0
    return time_enc(current)

def nxt(current):
    current = time_dec(current) + 10
    return time_enc(current)

def time_mx(current, video_len):
    return video_len if time_dec(current) > time_dec(video_len) else current

def op_skip(current, op_start, op_end):
    return op_end if time_dec(op_start) <= time_dec(current) <= time_dec(op_end) else current

def time_dec(current):
    return 60 * int(current[:2]) + int(current[3:])

def time_enc(current):
    mm = '0' + str(current//60) if current // 60 < 10 else str(current//60)
    ss = '0' + str(current%60) if current % 60 < 10 else str(current%60)
    return f'{mm}:{ss}'