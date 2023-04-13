def solution(begin, target, words):
    answer = 0
    
    # 한글자만 다른지 판별
    def diff_one(word1, word2):
        cnt = 0
        if len(word1) != len(word2):
            return False
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                cnt += 1
                if cnt >1:
                    return False
        if cnt == 1:
            return True
        else:
            return False
    
    def bfs(begin):
        # 1. 초기화
        from collections import deque
        q = deque([])
        visited = [-1]*len(words)
        
        # 2. 첫 input
        for i in range(len(words)):
            if visited[i] == -1 and diff_one(begin, words[i]):
                visited[i] = 1
                q.append([words[i],1])
        # 3. q돌리기
        while q:
            c_word, c_cnt = q.popleft()
            if c_word == target:
                return c_cnt
            
            for i in range(len(words)):
                if visited[i] == -1 and diff_one(c_word, words[i]):
                    visited[i] = 1
                    q.append([words[i],c_cnt+1])

        return 0
        
    answer = bfs(begin)
    
    return answer