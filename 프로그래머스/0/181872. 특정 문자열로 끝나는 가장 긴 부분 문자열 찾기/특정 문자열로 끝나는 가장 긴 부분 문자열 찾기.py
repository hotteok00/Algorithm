def solution(myString, pat):
    myString = myString[::-1]
    pat = pat[::-1]
    
    for i in range(len(myString)):
        if myString[i:].startswith(pat):
            return myString[i:][::-1]