# ㄷ자 형태라면 붙어있는 건지 구분이 안됨 -> 좌표*2로 사이 공간을 생성해서 해결
from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [[-1 for _ in range(102)] for _ in range(102)]
    visited = [[1 for _ in range(102)] for _ in range(102)]
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    q = deque()
    
    for r in rectangle:
        x1, y1, x2, y2 = map(lambda x: x*2, r)
        for i in range(x1, x2+1):
            for j in range(y1, y2+1):
                # x1, x2, y1, y2는 테두리이므로 제외하고 내부만 0으로 채움
                if x1 < i < x2 and y1 < j < y2:
                    graph[i][j] = 0
                # 다른 직사각형의 내부가 아니면서 테두리일 때 1로 채움
                elif graph[i][j] != 0:
                    graph[i][j] = 1                
    # 반복문을 마치면 테두리는 1, 내부는 0, 외부는 -1이 될 것이다   
    
    # 캐릭터와 아이템의 좌표도 2배씩 늘린다
    cx, cy, ix, iy = 2*characterX, 2*characterY, 2*itemX, 2*itemY
    
    q.append((cx, cy))
    
    while q:
        x, y = q.popleft()
        
        if x == ix and y == iy:
        	# 답을 반환할 때 2로 나누어 반환해준다
            answer = visited[x][y] // 2
            break   
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            
            if graph[nx][ny] == 1 and visited[nx][ny] == 1:
                visited[nx][ny] += visited[x][y]
                q.append((nx, ny))

    return answer