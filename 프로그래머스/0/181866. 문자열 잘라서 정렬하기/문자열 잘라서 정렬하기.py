def solution(myString):
    return sorted(x for x in myString.strip('x').split('x') if x != "")