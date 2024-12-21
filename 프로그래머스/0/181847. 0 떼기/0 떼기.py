def solution(n_str):
    for n_idx in range(len(n_str)):
        if n_str[n_idx] == '0':
            continue
        else:
            return ''.join(n_str[n_idx:])