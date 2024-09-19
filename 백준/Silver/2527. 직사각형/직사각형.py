for i in range(4):
    temp = list(map(int, input().split()))
    x1, y1, p1, q1 = temp[:4]
    x2, y2, p2, q2 = temp[4:]

    if (p1 < x2) or (p2 < x1) or (q1 < y2) or (q2 < y1):
        print('d')  # 공통부분이 없음
    elif (p1 == x2 and q1 == y2) or (p2 == x1 and q2 == y1) or (p1 == x2 and y1 == q2) or (x1 == p2 and q1 == y2):
        print('c')  # 점
    elif (p1 == x2) or (p2 == x1) or (q1 == y2) or (q2 == y1):
        print('b')  # 선분
    else:
        print('a')  # 직사각형
