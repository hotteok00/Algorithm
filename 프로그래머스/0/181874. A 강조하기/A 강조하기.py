def solution(myString):
    answer = ''
    for c in list(myString):
        if c.isupper():
            if c != 'A': 
                answer += c.lower()
            else:
                answer += c
        else:
            if c == 'a': 
                answer += 'A'
            else: 
                answer += c
    return answer