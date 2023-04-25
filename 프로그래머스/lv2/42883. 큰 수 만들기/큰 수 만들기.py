def solution(number, k):
    stack = []
    for i in number:
        while stack and stack[-1] < i and k > 0: 
            stack.pop() # 스택에서 마지막 숫자 제거
            k -= 1 # k 감소
        stack.append(i) # 스택에 현재 숫자 추가
    if k != 0: # "53421", 3의 경우엔 [5, 4, 2, 1]에 k가 2임
        stack = stack[:-k] # 스택의 마지막 k개의 숫자 제거
    return ''.join(stack)