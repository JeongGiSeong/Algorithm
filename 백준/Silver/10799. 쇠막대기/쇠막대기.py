import sys

read = sys.stdin.readline



# 괄호 시작부터 끝까지 레이저 개수 + 1을 하면 됨
string = list(read().strip())

ans = 0
stack = []
for i in range(len(string)):
    if string[i] == '(': # 여는 괄호면 stack에 추가
        stack.append('(')
    
    else: # 닫는 괄호
        if string[i - 1] == '(': # () -> 레이저
            stack.pop()
            ans += len(stack)
        else: # 쇠막대기 끝
            stack.pop()
            ans += 1

print(ans)
