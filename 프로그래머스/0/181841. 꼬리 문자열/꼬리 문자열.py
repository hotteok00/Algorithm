def solution(str_list, ex):
    return ''.join([str_ for str_ in str_list if check(str_, ex)])

def check(str_, ex):
    for i in range(0, len(str_) - len(ex) + 1):
        if str_[i:i + len(ex)] == ex: return False
    return True