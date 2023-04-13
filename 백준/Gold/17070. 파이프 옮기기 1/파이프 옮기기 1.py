# 일단 dfs 구현

# 가로로 놓여진 경우 -> 가로 & 대각
# 가로로 움직이는 경우 : lu=(lu_r, lu_c), ru=(ru_r, ru_c)  => new_lu = (ru_r, ru_c), new_ru = (ru_r, ru_c+1)
# 대각으로 움직이는 경우
#  lu_r, lu_c, ru_r, ru_c => new_lu = (ru_r, ru_c), new_ru = (ru_r, ru_c+1)
#                         => new_ld = (ru_r+1, ru_c), new_rd = (ru_r+1, ru_c+1)

# 세로로 놓여진 경우 -> 세로 & 대각
# lu=(lu_r, lu_c), ld=(ld_r, ld_c) => new_lu


# 대각으로 놓여진 경우 -> 가로 & 세로 & 대각


# 생각해보니 그냥 끝점 좌표만 알고 있으면 됨
import sys
input = sys.stdin.readline
def dfs(cr,cc,d): #현재 상태로, 현재 끝점의 cr,cc 위치 / 놓여진 방향  d = 0: 가로, d=1:세로, d=2: 대각
    global count
    # print('이동경로',cr,cc,d)
    if cr == N-1 and cc == N-1:
        count+=1
        # print('d is ', d)
        return

    else:
        # 현재 가로나 대각선인 경우 => 가로이동
        if d == 0  or d == 2:
            # 가로 이동
            nr = cr
            nc = cc +1
            if nc < N and arr[nr][nc] == 0:
                dfs(nr,nc,0)



        # 현재가 세로나 대각선인 경우 => 세로이동
        if d == 1 or d == 2:
            # 세로이동
            nr = cr +1
            nc = cc
            if nr < N and arr[nr][nc] == 0:
                dfs(nr,nc,1)


        # 대각이동
        nr = cr + 1
        nc = cc + 1
        if nr < N and nc < N and arr[nr][nc] == 0 and arr[nr-1][nc] == 0 and arr[nr][nc-1] == 0:
            dfs(nr,nc,2)


N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
count = 0
dfs(0,1,0) # 가로로 시작

print(count)
