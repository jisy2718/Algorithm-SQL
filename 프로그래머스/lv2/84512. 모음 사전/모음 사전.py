def solution(word):
    answer = 0
    
    alpha_orders = ['A','E','I','O','U']
    
    
    # 1. 순서대로 순회
    def recursion(cur_word):
        nonlocal answer
        
        answer += 1
        ## 1. baseline 1 : 성공
        if cur_word == word:
            return True
        
        ## 2. baseline 2 : 실패
        if len(cur_word) == 5:
            return False
        
        
        ## 3. 재귀호출
        for alpha in alpha_orders:
            if recursion(cur_word+alpha) == True:
                return True   # 재귀호출 위쪽으로 모두 True를 보내기 위해서 True return
        
        
    # 2. 알파벳 순서대로 넣기
    for alpha in alpha_orders:
        # 3. 해당 알파벳으로 시작하게 된다면, 몇번째에 해당하는지 answer에 저장되어있고, True를 return하게 됨.
        if recursion(alpha) == True:
            return answer
    