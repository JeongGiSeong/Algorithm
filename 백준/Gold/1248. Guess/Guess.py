import sys, time
read = sys.stdin.readline
# start = time.time()
# end = time.time()
# print(f"{end - start:.5f} sec")


n = int(input())
s = input()
matrix = [[' '] * n for _ in range(n)]
stack = []

cnt = 0
for i in range(n):
    for j in range(i, n):
        matrix[i][j] = s[cnt]
        cnt += 1


def dfs(depth: int):
    # 가지치기
    total = 0
    for i in range(depth - 1, -1, -1):
        total += stack[i]
        if matrix[i][depth - 1] == "0":
            if total != 0:
                return
        elif matrix[i][depth - 1] == "-":
            if total >= 0:
                return
        elif matrix[i][depth - 1] == "+":
            if total <= 0:
                return
                
    if depth == n:
        print(*stack)
        # return
        exit()
    
    for i in range(11):
        if matrix[depth][depth] == '-':
            stack.append(i * -1)
        elif matrix[depth][depth] == '0':
            stack.append(0)
        else:
            stack.append(i)
        
        dfs(depth + 1)
        stack.pop()
    

dfs(0)