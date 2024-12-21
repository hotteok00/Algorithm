def solution(binomial):
    splited = binomial.split(" ")
    
    a = int(splited[0])
    b = int(splited[2])
    
    if   splited[1] == "+": return a + b
    elif splited[1] == "-": return a - b
    else:                   return a * b