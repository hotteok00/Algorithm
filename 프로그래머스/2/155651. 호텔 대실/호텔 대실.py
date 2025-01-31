def solution(book_time):
    book_time.sort()
    
    cleanUpTime = 10
    for idx, (start, end) in enumerate(book_time):
        book_time[idx] = [cal_time(start), cal_time(end) + cleanUpTime]
    
    rooms = []
    max_rooms = 0
    for idx_b, (start, end) in enumerate(book_time):
        for idx_r, room in enumerate(rooms):
            if room <= start:
                rooms[idx_r] = end
                borrow = True
                break
        else:
            rooms.append(end)
            max_rooms += 1
        
    return max_rooms

def cal_time(time):
    h, m = time.split(":")
    return 60 * int(h) + int(m)