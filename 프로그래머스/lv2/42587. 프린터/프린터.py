def solution(priorities, location):
    answer= 0
    from collections import deque

    d = deque([(v,i) for i,v in enumerate(priorities)])

    while True:
        item = d.popleft()
        # 마지막 문서일 경우 max() 사용 시 오류 발생
        if d and max(d, key=lambda x: x[0])[0] > item[0]:
            d.append(item)
        else:
            answer += 1
            if item[1] == location:
                break
    return answer