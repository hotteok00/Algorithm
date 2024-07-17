def get_win_rate(x, y):
    return y * 100 // x

def find_min_games(x, y):
    initial_rate = get_win_rate(x, y)
    
    if initial_rate >= 99:  # 승률이 99% 이상이면 승률을 올릴 수 없음
        return -1

    left, right = 0, 10**9
    answer = -1

    while left <= right:
        mid = (left + right) // 2
        new_x = x + mid
        new_y = y + mid
        new_rate = get_win_rate(new_x, new_y)
        
        if new_rate > initial_rate:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    return answer

# 입력 받기
import sys
input = sys.stdin.readline

x, y = map(int, input().split())
print(find_min_games(x, y))
