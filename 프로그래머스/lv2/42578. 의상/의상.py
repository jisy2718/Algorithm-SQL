def solution(clothes):
    answer = 0
    
    clothes_num = {}
    for lst in clothes:
        _ , cloth_type = lst
        if cloth_type in clothes_num:
            clothes_num[cloth_type] += 1
        else:
            clothes_num[cloth_type] = 1
    
    comb = 1
    for cloth_type, num in clothes_num.items():
        comb *= (num+1)
    
    answer = comb -1
            
    return answer