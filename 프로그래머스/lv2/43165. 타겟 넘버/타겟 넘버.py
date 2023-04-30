def solution(numbers, target):
    answer = 0
    
    def dfs(cur_idx, cur_sum):
        nonlocal answer
        # 마지막까지 연산한 경우
        if cur_idx == len(numbers)-1:
            if cur_sum == target:
                answer += 1
            
            return
        
        # 다음 숫자 탐색
        next_num = numbers[cur_idx+1]
        dfs(cur_idx+1, cur_sum + next_num)
        dfs(cur_idx+1, cur_sum - next_num)
        
    
    dfs(0, numbers[0])
    dfs(0, -numbers[0])
    
    return answer