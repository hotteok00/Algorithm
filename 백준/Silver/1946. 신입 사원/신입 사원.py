from sys import stdin, stdout
input = stdin.readline
output = stdout.write

T = int(input())

for _ in range(T):
    ans = 0
    
    N = int(input())
    candidates = []
    for idx in range(N):
        screening_scores, interview_scores = map(int, input().split())
        candidates.append((screening_scores, interview_scores))
    
    # 서류심사 성적 내림차순 정렬 후 면접 성적 비교
    candidates.sort(key=lambda x: x[0], reverse=True)
    
    min_score = candidates[N-1][1]
    for i in range(N-2, -1, -1):
        if min_score > candidates[i][1]:
            min_score = candidates[i][1]
        else:
            ans += 1
    
    output(str(N - ans) + "\n")