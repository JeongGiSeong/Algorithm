import sys, time
read = sys.stdin.readline
# start = time.time()
# end = time.time()
# print(f"{end - start:.5f} sec")


# n행, m열
n, m = map(int, input().split())

paper = []
for _ in range(n):
    paper.append(list(map(int, input())))

ans = 0

# ** 0이면 세로, 1이면 가로로 가정 **
for i in range(1 << n*m):
    total = 0
    #가로합 계산
    for row in range(n):
        rowsum = 0
        for col in range(m):
            # idx는 2차원 행렬을 1줄로 만들었을때의 인덱스
            idx = row*m + col
            if i & (1 << idx) != 0: #(0아니면 가로로 더한다)
                rowsum = rowsum * 10 + paper[row][col]
            else:
                total += rowsum
                rowsum = 0
        total += rowsum

    #세로합 계산
    for col in range(m):
        colsum = 0
        for row in range(n):
            idx = row*m + col
            if i & (1 << idx) == 0: #(0이면 세로로 더한다)
                colsum = colsum * 10 + paper[row][col]
            else:
                total += colsum
                colsum = 0
        total += colsum

    ans = max(ans, total)

print(ans)
