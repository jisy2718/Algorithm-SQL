def solution(tickets):
    answer  = []
    length  = len(tickets) + 1
    results = []
    
    # {출발공항 : [도착공항들]} 인 딕셔너리 만들어서 연결관계 표기
    ticket_dict = {}
    for ticket in tickets:
        start = ticket[0]
        end = ticket[1]
        if start not in ticket_dict:
            ticket_dict[start] = [end]
        else:
            ticket_dict[start].append(end)
            ticket_dict[start].sort()  # dfs 탐색시 알파벳이 빠른 순서대로 탐색하게 하기 위해
        
        if end not in ticket_dict:
            ticket_dict[end] = []
    
    # ticket_dict와 마찬가지 형태로 visited dict 생성
    visited = {}
    for cur_airport, next_airport_lst in ticket_dict.items():
        visited[cur_airport] = [0]*len(next_airport_lst)
            
    cur_airport = 'ICN'
    def dfs(cur_airport :str, visited:dict, path:list):
        for i in range(len(ticket_dict[cur_airport])):
            next_airport = ticket_dict[cur_airport][i]
            visit = visited[cur_airport][i]
            if visit == 0:
                visited[cur_airport][i] = 1
                path.append(next_airport)
                dfs(next_airport, visited, path)
                # dfs에서 나온 것은 해당 티켓 사용한 탐색이 끝났다는 것이므로, 다시 원상복귀해서 다시 티켓 사용할 수 있도록 초기화
                visited[cur_airport][i] = 0
                path.pop()
                
                
        # 목표지점에 도달한 경우
        if len(path) == length:
            # print(len(path), length)
            # print(path)
            result = path.copy()
            answer.append(result)
            

    
    dfs(cur_airport, visited, ['ICN'])
    
    
    return answer[0]




# def solution(tickets):
    
#     # {출발공항 : [도착공항들]} 인 딕셔너리 만들어서 해결 (힙 이용하면 더 빠르게 할 수 있음)
#     ticket_dict = {}
#     for ticket in tickets:
#         start = ticket[0]
#         end = ticket[1]
#         if start not in ticket_dict:
#             ticket_dict[start] = [end]
#         else:
#             ticket_dict[start].append(end)
#             ticket_dict[start].sort(reverse=True)  # pop()했을 때 알파벳 제일 앞선 것 나오게 하기 위해
    
    
#     # 순회
#     cur_airport = 'ICN'    
#     answer = [cur_airport]
    
#     length = len(tickets) # 티켓길이만큼 반복
#     while length != 0:
#         next_airport = ticket_dict[cur_airport].pop()
#         answer.append(next_airport)
#         length -=1
#         cur_airport = next_airport
        
    
#     return answer