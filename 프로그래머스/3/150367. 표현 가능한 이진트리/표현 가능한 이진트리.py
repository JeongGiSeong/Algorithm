# 42 이진수 = 101010
# 완전이진트리로 바꾸려면 2^h-1
# 따라서 6 < 2^3-1이므로 h는 3
# 완전이진트리로 만드려면 앞자리에 그 수만큼 0을 붙이면 됨
# 0101010. 이제 이게 맞는 완전이진트리인가를 확인해야됨
# 부모 노드가 0이면 자식들도 무조건 0. 
import math

def check(b, parent):
    # 부모가 0이면 자식도 전부 0이여야 됨
    if parent == '0':
        if '1' in b:
            return 0

    if len(b) == 1:
        return 1
    center = len(b)//2
    return check(b[:center], b[center]) and check(b[center+1:], b[center])

def solution(numbers):
    answer = []
    
    for num in numbers:
        # 2진수 변환
        num_bin = bin(num)[2:]
        # 2^n - 1꼴의 자릿수를 가져야함.
        digit = 2 ** (int(math.log(len(num_bin), 2)) + 1) - 1
        num_bin = "0" * (digit - len(num_bin)) + num_bin
        # print(digit, num_bin)
        
        answer.append(check(num_bin, num_bin[len(num_bin)//2]))
    # print(answer)
    return answer