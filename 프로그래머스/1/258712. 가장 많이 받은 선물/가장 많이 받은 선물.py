def solution(friends, gifts):
    received, will_receive, sender_receiver = {}, {}, {}
    for friend in friends:
        received[friend] = 0
        will_receive[friend] = 0
        sender_receiver[friend] = []
    
    for gift in gifts:
        sender, receiver = gift.split(" ")
        received[receiver] += 1
        sender_receiver[sender].append(receiver)
    
    for sender, receivers in sender_receiver.items():
        # print(sender, receivers)
        for other in sender_receiver.keys():
            if other == sender: continue
            
            sender_to_other = counter(receivers, other)
            other_to_sender = counter(sender_receiver[other], sender)
            
            if sender_to_other < other_to_sender:
                will_receive[other] += 1
            elif sender_to_other > other_to_sender:
                will_receive[sender] += 1
            else:   # gift-index compare=
                sender_gift_index = gift_index(receivers, received[sender])
                ohter_gift_index = gift_index(sender_receiver[other], received[other])
                
                if sender_gift_index < ohter_gift_index:
                    will_receive[other] += 1
                elif sender_gift_index > ohter_gift_index:
                    will_receive[sender] += 1
        
#     print(received)
#     print(will_receive)
#     print(sender_receiver)
    
    for name, count in will_receive.items():
        will_receive[name] = count // 2
    
    return max(will_receive.values())

def counter(arr, target):
    return len([i for i in arr if i == target])

def gift_index(gave_arr, received_count):
    return len(gave_arr) - received_count