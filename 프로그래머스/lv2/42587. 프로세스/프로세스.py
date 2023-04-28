def solution(priorities, location):
    answer = 0
    
    # q를 이용해 priorities 나타내기
    from collections import deque
    q = deque([])
    for loc in range(len(priorities)):
        q.append([priorities[loc], loc]) # [값, 처음위치]
    
    # priorities를 순회하기
    answer = 0
    while q:
        c_prior, c_loc = q.popleft()
        # 우선순위 판정
        if q:
            for prior, loc in q:
                if prior > c_prior:
                    q.append([c_prior, c_loc])  # 자신보다 우선순위 높은 것 있다면, 다시 q에 넣고 처음부터 반복
                    break
            else:
                answer += 1
                # 만약 목표 지점인 경우 break
                if c_loc ==location:
                    break
                    
        else: # q비어있다면, 현재 원소가 실행될 차례이고, 그것이 location 원소
            answer += 1
            break
    
    return answer