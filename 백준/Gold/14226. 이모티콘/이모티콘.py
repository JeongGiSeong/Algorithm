import sys
from collections import deque
read = sys.stdin.readline


# 2초 512MB
# 화면에 1개 기본

S = int(read())
q = deque([[1, 0, 0]])
visited = [[False] * 1001 for _ in range(1001)]
visited[1][0] = True

while q:
    screen, clip, cnt = q.popleft()

    if screen == S:
        print(cnt)
        exit()
        
    for i in range(3):
        # 복사
        if i == 0:
            new_screen, new_clip = screen, screen
        #붙여넣기
        elif i == 1:
            new_screen, new_clip = screen + clip, clip
        elif i == 2:
            new_screen, new_clip = screen - 1, clip
        
        if 0<=new_screen<1001 and 0<=new_clip<1001 and not visited[new_screen][new_clip]:
            visited[new_screen][new_clip] = True
            q.append([new_screen, new_clip, cnt + 1])