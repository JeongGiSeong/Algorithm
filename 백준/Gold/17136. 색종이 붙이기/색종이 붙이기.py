# 5x5부터 시작해서 1x1까지 그리드를 사용해서 풀자
# 그리드로 안되는 상황이 있나? 없다.

import sys
input = sys.stdin.readline

paper = [list(map(int, input().split())) for _ in range(10)]
ans = 25
cnt = [0] * 6

def is_possible(y, x, size):
    if cnt[size] == 5:
        return False

    if y+size > 10 or x+size > 10:
        return False

    for i in range(size):
        for j in range(size):
            if paper[y+i][x+j] == 0:
                return False

    return True

def mark(y, x, size, v):
    for i in range(size):
        for j in range(size):
            paper[y+i][x+j] = v

def backtraking(y, x):
    global ans

    if y == 10: # 10x10을 전부 탐색한 경우
        ans = min(ans, sum(cnt))
        return
    
    if x == 10:
        backtraking(y+1, 0)
        return
    
    if paper[y][x] == 0:
        backtraking(y, x+1)
        return

    for size in range(1, 6):
        if is_possible(y, x, size):
            mark(y, x, size, 0)
            cnt[size] += 1
            backtraking(y, x+1)
            mark(y, x, size, 1)
            cnt[size] -= 1

backtraking(0, 0)
print(-1 if ans == 25 else ans)