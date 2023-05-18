N = int(input())

white = [[0]*100 for _ in range(100)]

for _ in range(N):
    left, down = map(int,input().split())
    
    for c in range(left,left+10):
        for r in range(down, down+10):
            white[r][c] = 1
result = 0
for r in range(100):
    for c in range(100):
        result += white[r][c]
print(result)