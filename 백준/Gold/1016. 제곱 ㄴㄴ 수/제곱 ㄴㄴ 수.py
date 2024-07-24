import sys
import math

input = sys.stdin.readline

def count_non_squarefree(A, B):
    # A부터 B까지 모든 수가 제곱 ㄴㄴ수인지 체크할 배열
    is_squarefree = [True] * (B - A + 1)
    
    # 2부터 sqrt(B)까지의 모든 수에 대해 반복
    for i in range(2, int(math.sqrt(B)) + 1):
        square = i * i
        start = max(square, (A + square - 1) // square * square)
        
        for j in range(start, B + 1, square):
            is_squarefree[j - A] = False
    
    return sum(is_squarefree)

# 입력 받기
A, B = map(int, input().split())

# 제곱 ㄴㄴ수 개수 세기
result = count_non_squarefree(A, B)

# 결과 출력
print(result)
