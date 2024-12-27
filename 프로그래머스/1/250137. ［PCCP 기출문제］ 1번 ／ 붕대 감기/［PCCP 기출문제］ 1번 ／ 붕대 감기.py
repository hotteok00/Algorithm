def solution(bandage, health, attacks):
    time = 0
    attack_idx = 0
    current_hp = health
    continunity = 0
    
    last_attack_time = attacks[-1][0]
    while time <= last_attack_time:
        # if 공격 받음?
        # elif 최대 체력?
        # else 붕대 감기 & 체력 회복
        
        if attacks[attack_idx][0] == time: # attacked
            # get damaged
            current_hp -= attacks[attack_idx][1]
            if current_hp <= 0: return -1
            
            continunity = 0
            attack_idx += 1
        elif current_hp != health:
            # recovery per second & additional recovery
            current_hp += bandage[1]
            continunity += 1
            
            if continunity == bandage[0]:
                current_hp += bandage[2]
                continunity = 0
            
            if current_hp > health:
                current_hp = health
        
        time += 1
    
    return current_hp