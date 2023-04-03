N = int(input())
# 트리 생성
tree = {}
for _ in range(N):
    p,c1, c2 = input().split()
    tree[p] = [c1,c2]


# 순회함수 생성
def traversal(cur_node, order):
    # 만약 자식이 없는 곳에 왔다면 return
    if cur_node == '.':
        return

    # 전위순회의 경우 부모부터 순회하는 것!
    if order == 'pre':
        print(cur_node, end='')

    # 왼쪽 자식으로 이동
    traversal(tree[cur_node][0], order)

    # 중위순회의 경우, 왼쪽 자식을 순회한 이후에 순회하는 것
    if order =='mid':
        print(cur_node, end='')

    # 오른쪽 자식으로 이동
    traversal(tree[cur_node][1], order)

    # 후위순회의 경우, 양쪽 자식을 순회한 이후에 순회하는 것
    if order =='post':
        print(cur_node, end='')

    return

# 순회하기
traversal('A','pre')  # 전위
print()
traversal('A','mid')  # 중위
print()
traversal('A','post') # 후위