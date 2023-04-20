# def solution(numbers):
#     numbers = list(map(str, numbers))
#     # 3을 곱하는 이유 -> numbers의 원소는 0 이상 1,000 이하
#     # 한 자리 수도 3자리로 만들어서 정렬해야 함
#     # 문자열 정렬은 일의자리부터 비교. 
#     # [3, 30, 31] -> [333, 3030, 3131] -> [333, 0303, 1313] = 333 > 1313 > 0303. 즉 3, 31, 30 순으로 정렬됨.
#     numbers.sort(key=lambda x: x*3, reverse=True)
#     return str(int(''.join(numbers)))

import functools

def comparator(a,b):
    t1 = a+b
    t2 = b+a
    #  t1이 크다면 1-0 = 1  // t2가 크다면 0-1 = -1  //  같으면 0-0 = 0
    return (int(t1) > int(t2)) - (int(t1) < int(t2)) 

def solution(numbers):
    n = [str(x) for x in numbers]
    n = sorted(n, key=functools.cmp_to_key(comparator),reverse=True)
    answer = str(int(''.join(n)))
    return answer