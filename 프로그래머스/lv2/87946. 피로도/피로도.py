def check(k,go_dungeon):
    count = 0
    for dungeon in go_dungeon:
        need, use = dungeon
        # 던전을 돌 수 있다면 돌기
        if k >= need:
            k -= use
            count += 1
        # 던전 돌 수 없다.
        else:
            count = 0
            break
    
    return count

def solution(k, dungeons):
    # 1. 순열만드는 함수 생성
    def perm(idx, r):
        nonlocal answer
        if idx == r:
            count = check(k, go_dungeon)
            if answer < count:
                answer = count
            return

        for i in range(len(dungeons)):
            if used[i] == 0:
                used[i] = 1
                go_dungeon[idx] = dungeons[i]
                perm(idx+1, r)
                used[i] = 0
    
    
    used = [0]* len(dungeons)
    answer = 0
    for r in range(1, len(dungeons)+1):
        go_dungeon = [0]*r
        perm(0, r)
        
    
    return answer