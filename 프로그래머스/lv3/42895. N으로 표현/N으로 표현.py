def solution(N, number):
    answer = 0
    INF = 10
    upper_bound = 32000
    dp = [INF]*(upper_bound+1)  # idx : 숫자, value : cnt
    
    # Ak를 k개로 만들 수 있는 숫자들 개수라고 한다면, 
    # A1 = 1 , : 5를 만들 수 있음
    # A2 = 1 + (A1 과 A1 사칙연산 중 새로 cnt 된 숫자 수) : 55, A1 & A1 간의 사칙연산 = 5+5, 5/5, 5*5
    # A3 = 1 + (A2와 A1 사칙연산 중 새로 cnt 된 숫자 수) : 555 , A1 & A2 간의 사칙연산
    
    def make_continues_num(N, cnt):
        result = 0
        while cnt > 0:
            result = result*10 + N
            cnt -= 1
        return result
    
#     dp[N] = 1
#     for cnt in range(2,9):
#         continues_num = make_continues_num(N, cnt)
#         if continues_num <= number:
#             dp[continues_num] = cnt
#         for num1 in range(1,number):
#             for num2 in range(num1, number+1):
#                 if dp[num1] + dp[num2] == cnt:  # num1과 num2가 총 cnt만큼 N을 사용했다면 사칙연산 진행
#                     plus = num1 + num2
#                     minus = num2 - num1
#                     product = num1 * num2
#                     div = num2//num1
#                     oper_results = [plus, minus, product, div]
#                     for oper_result in oper_results:
#                         if 1 <= oper_result <= number and dp[oper_result] > cnt:
#                             dp[oper_result] =  cnt
    
    
    dp_dict = {x : set() for x in range(1, 9)}
    dp_dict[1].add(N)
    dp[N] = 1
    for cnt in range(2,9):
        continues_num = make_continues_num(N, cnt)
        if continues_num <= upper_bound:
            dp_dict[cnt].add(continues_num)
            dp[continues_num] = cnt
        
        for i in range(1, cnt):
            j = cnt - i
            
            # 각 ai와 aj에서 가능한 사칙연산 모두 진행
            ai = dp_dict[i]
            aj = dp_dict[j]
            for num1 in ai:
                for num2 in aj:
                    plus = num1 + num2
                    minus1 = num2 - num1
                    minus2 = num1 - num2
                    product = num1 * num2
                    div1 = num2//num1
                    div2 = num1//num2
                    oper_results = [plus, minus1, minus2, product, div1, div2]          
                    for oper_result in oper_results:
                        if 1 <= oper_result <= upper_bound : # 숫자가 범위 내이고
                            # 이전에 나오지 않은 숫자이면 gogo!
                            if dp[oper_result] > cnt:
                                dp[oper_result] = cnt
                                dp_dict[cnt].add(oper_result)
    answer = dp[number]
    if answer > 8:
        answer = -1
    return answer
                    