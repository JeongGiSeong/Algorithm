import sys
from collections import deque
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input()) # 편의점 개수
    home = tuple(map(int, input().split()))
    store = []
    for _ in range(n):
        store.append(tuple(map(int, input().split())))
    festival = tuple(map(int, input().split()))

    # 50m에 맥주 1병, 상자엔 최대 20병, 편의점에서 리필
    # 두 좌표 사이의 거리는 x 좌표의 차이 + y 좌표의 차이
    # 경로를 어떻게 정해야 하는 거지? -> BFS

    visited = [False] * (n + 1)
    q = deque()
    q.appendleft(home)
    while q:
        x, y = q.popleft()
        if abs(x-festival[0]) + abs(y-festival[1]) <= 1000:
            print('happy')
            break

        for i in range(n):
            if not visited[i]:
                nx, ny = store[i]
                if abs(x-nx) + abs(y-ny) <= 1000:
                    visited[i] = True
                    q.append((nx, ny))
    else:
        print('sad')