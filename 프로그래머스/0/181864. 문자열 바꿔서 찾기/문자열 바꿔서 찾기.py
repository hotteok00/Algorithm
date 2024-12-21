def solution(myString, pat):
    temp = []
    for c in myString:
        temp.append('A' if c == 'B' else 'B')

    if pat in ''.join(temp):
        return 1
    else:
        return 0