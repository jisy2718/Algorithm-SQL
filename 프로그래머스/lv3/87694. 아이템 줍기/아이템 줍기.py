def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    n = 50*2 + 1
    # 값을 2배하여, 2칸씩 움직이는 것이 1단위로 세도록 코딩함. -> 그래서 모든 사각형이 내부에 자연수 점을 가지도록 코딩함
    # ----- 준비 ------
    # 1. 사각형 변위인지 여부 배열
    is_line = [[0]*n for _ in range(n)]
    for x in range(1,n):
        for y in range(1,n):
            for rec in rectangle:
                rec = [x*2 for x in rec]
                lbx, lby, rtx, rty = rec # 좌하x, 좌하y, 우상x, 우상y
                if (x in [lbx,rtx]  and lby <= y <= rty) or (y in [lby, rty] and lbx <= x <= rtx):
                    is_line[y][x] = 1   
    # for row in is_line:
    #     print(row)
        
    # def is_same_line(cx,cy, nx,ny):
    #     # 현재와 다음 지점 모두가 같은 rectangle 위에 있는지 파악
    #     for rec in rectangle:
    #         lbx, lby, rtx, rty = rec # 좌하x, 좌하y, 우상x, 우상y
    #         if (cx in [lbx,rtx]  and lby <= cy <= rty) or (cy in [lby, rty] and lbx <= cx <= rtx):  # 현재 rectangle
    #             if (nx in [lbx,rtx]  and lby <= ny <= rty) or (ny in [lby, rty] and lbx <= nx <= rtx): # 현재 rectangle
    #                 return True
    #     return False
        
    # 2. 다른 사각형 내부를 지나지 않도록 이동 : 필요한 것은 사각형 내부인지 파악하는 코드(2차원 배열이용)
    is_inner = [[0]*n for _ in range(n)] # 1이면 inner
    for x in range(1,n):
        for y in range(1,n):
            for rec in rectangle:
                rec = [x*2 for x in rec]
                lbx, lby, rtx, rty = rec # 좌하x, 좌하y, 우상x, 우상y
                if lbx < x < rtx and lby < y < rty:
                    is_inner[y][x] = 1
    # for row in is_inner:
    #     print(row)
    
#     def is_same_rec_other_line(cx,cy, nx,ny):  # 내부칸크기가 1인 경우 해당 사각형 관통하는 것 방지
#         for rec in rectangle:
#             lbx, lby, rtx, rty = rec # 좌하x, 좌하y, 우상x, 우상y
#             if (cx in [rtx]  and lby <= cy <= rty) :  # 현재 rectangle
#                 if (nx in [lbx]  and lby <= ny <= rty): # 현재 rectangle
#                     return True
                
#             if (cy in [ rty] and lbx <= cx <= rtx):  # 현재 rectangle
#                 if  (ny in [lby] and lbx <= nx <= rtx): # 현재 rectangle
#                     return True               
                
#             if (cx in [lbx]  and lby <= cy <= rty) :  # 현재 rectangle
#                 if (nx in [rtx]  and lby <= ny <= rty) : # 현재 rectangle
#                     return True
                
#             if (cy in [lby] and lbx <= cx <= rtx):  # 현재 rectangle
#                 if (ny in [rty] and lbx <= nx <= rtx): # 현재 rectangle
#                     return True
#         return False
                
    # 3. visited 배열이용해서 간 곳 다시 안가도록
    visited = [[0]*n for _ in range(n)]
    
    # ------ bfs 시작 ------
    from collections import deque
    move_cnt = 0
    q = deque([[characterX*2,characterY*2,move_cnt]])
    visited[characterY*2][characterX*2] = 1
    while q:
        print(q)
        cx, cy, c_cnt = q.popleft()
        if cx ==itemX*2 and cy == itemY*2:
            answer = c_cnt
            break
        # 이동할 수 있는 모든 경우 탐색 
        for dx, dy in [[0,2],[0,-2],[2,0],[-2,0]]:
            nx = cx + dx
            ny = cy + dy
            midx = cx + dx//2
            midy = cy + dy//2
            # 사각형의 변위에 있는지 판단 & 다른 사각형 내부를 지나지 않도록 이동
            if 0 < nx < n and 0 < ny < n and is_line[midy][midx] == 1 and is_line[ny][nx] == 1 and is_inner[midy][midx] == 0 and is_inner[ny][nx] == 0 and visited[ny][nx] == 0 :
                visited[ny][nx] = 1
                q.append([nx,ny, c_cnt +1])
                
     
    return answer