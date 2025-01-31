def solution(w):
    u, v = split(w)
    # print(f'u = {u}, v = {v}')
    
    if u == '': return u
    
    if is_right(u):
        return u + solution(v)
    else:
        return '(' + solution(v) + ')' + ''.join(list(flip(u[1:-1])))
    
def split(w):
    count = 0
    for i in range(len(w)):
        if w[i] == '(': 
            count += 1
        else:
            count -= 1
            
        if count == 0:
            if i+1 < len(w):
                return w[:i+1], w[i+1:]
            else:
                return w, ''
    return w, ''
    
def is_right(w):
    stack = []
    for i in w:
        if i == '(':
            stack.append(i)
        elif i == ')' and len(stack) > 0 and stack[-1] == '(':
            stack.pop()
        else:
            return False
    return True if len(stack) == 0 else False

def flip(w):
    w_list = list(w)
    for i in range(len(w_list)):
        w_list[i] = '(' if w_list[i] == ')' else ')'
    return ''.join(w_list)