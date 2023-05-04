from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    
    
    truck_weights = deque(truck_weights)
    
    # 1초 후
    answer += 1
    cur_truck = truck_weights.popleft()
    on_bridge = deque([[bridge_length, cur_truck]])
    sum_weight = cur_truck  # 다리 위 전체 무게
    num_truck = 1           # 다리 위 트럭 개수
    while on_bridge:
        # print(on_bridge, answer)
        
        # 1초 후
        answer += 1
        for time_truck in on_bridge:
            time_truck[0] -= 1
            
        # 다 건넌 트럭
        if on_bridge[0][0] == 0: # 맨 앞의 트럭이 다리를 다 건넜다면,
            time, truck = on_bridge.popleft()
            sum_weight -= truck
            num_truck -= 1
        

        # 새로운 트럭 올릴 수 있으면 올리기
        if truck_weights and num_truck < bridge_length: # 새로운 트럭이 있고, 다리가 꽉차지 않았다면,
            # print('1')
            if truck_weights[0] + sum_weight <= weight:  # 새로운 트럭과 기존 다리위 트럭의 무게가 한도 무게 이하라면 추가
                
                new_truck = truck_weights.popleft()
                sum_weight += new_truck
                # print(new_truck, sum_weight, weight)
                on_bridge.append([bridge_length, new_truck])
        # print()
        # print(on_bridge)

        # print(on_bridge)   
        
    return answer