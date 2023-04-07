import sys
sys.setrecursionlimit(10 ** 9)
# 1. input
pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    except:
        break
        
# root를 찾고, root보다 작은 수들은 왼쪽트리, root보다 큰 수들은 오른쪽 트리

def post(start, end):
    # 1.base case
    if start > end:
        return
    
    # 2. recursion case
    cur_root = pre_order[start]
    
    right_root = end + 1 # right_root가 없는 경우 왼편 트리의 마지막이 end가 되도록
    for i in range(start+1, end+1):
        if cur_root < pre_order[i]:
            right_root = i
            break # 찾으면 그것이 오른쪽 루트이므로, 바로 break
    # 왼편
    post(start+1, right_root -1)  # 왼쪽 트리가 없다면 start + 1, (start+1) -1 이 되어 index 역전
    # 오른편
    post(right_root, end)         # 오른편 트리가 없다면 , end + 1, end 가 되어 index 역전
    print(cur_root, end= ' ')

post(0,len(pre_order)-1)
    
    
    
        