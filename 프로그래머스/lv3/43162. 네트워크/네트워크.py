
    


def solution(n, computers):
    # 1. dfs 함수 정의
    def dfs(com):
        # 이웃 중에 방문안한 곳 방문 후 탐색
        for neighbor in range(n):
            if computers[com][neighbor] == 1 and visited[neighbor] == 0:
                visited[neighbor] = 1
                dfs(neighbor)
        
        return
    
    # 2. 연결영역 개수 & visited 초기화
    answer = 0
    visited = [0]*n
    
    # 3. 순회하며 방문안한 곳 방문
    for com in range(n):
        if visited[com] == 0:
            visited[com] = 1
            answer += 1
            dfs(com)
    return answer