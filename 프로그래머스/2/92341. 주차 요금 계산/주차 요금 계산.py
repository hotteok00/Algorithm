def solution(fees, records):
    answer = []
    
    records_by_car = {}
    for record in records:
        time, car, dsc = record.split()
        if car not in records_by_car:
            records_by_car[car] = []
        records_by_car[car].append((time, dsc))
    
    for car, value in sorted(records_by_car.items()):
        if value[-1][1] == 'IN':
            records_by_car[car].append(('23:59', 'OUT'))
        total_time = cal_time(value)
        fee = cal_fee(total_time, fees)
        answer.append(fee)
    
    return answer

def cal_time(time_list):
    total_time = 0
    for idx in range(len(time_list)-1, -1, -2):
        OUT_h, OUT_m = time_list[idx][0].split(':')
        IN_h, IN_m = time_list[idx-1][0].split(':')
        OUT = int(OUT_h) * 60 + int(OUT_m)
        IN = int(IN_h) * 60 + int(IN_m)
        total_time += OUT - IN
    return total_time

def cal_fee(total_time, fees):
    base_time, base_fee, u_time, u_fee = fees
    if total_time <= base_time:
        return base_fee
    else:
        if (total_time - base_time) // u_time == (total_time - base_time) / u_time:
            return base_fee + ((total_time - base_time) // u_time) * u_fee
        else:
            return base_fee + (((total_time - base_time) // u_time) + 1) * u_fee