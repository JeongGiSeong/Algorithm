def solution(numbers):
    numbers = list(map(str, numbers))
    # 3을 곱하는 이유 -> numbers의 원소는 0 이상 1,000 이하
    # 한 자리 수도 3자리로 만들어서 정렬해야 함
    # 문자열 정렬은 사전순. 
    # [3, 30, 31] -> [333, 3030, 3131] -> [333, 0303, 1313] = 333 > 1313 > 0303. 즉 3, 31, 30 순으로 정렬됨.
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))