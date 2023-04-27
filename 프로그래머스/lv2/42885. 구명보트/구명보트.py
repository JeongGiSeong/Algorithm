def solution(people, limit):
    answer = 0
    people.sort()
    
    # 하나에 최대 2명, 무게 제한(limit)
    s, e = 0, len(people) - 1
    while s < e:
        if people[s] + people[e] <= limit:
            s += 1
            # answer : 2명이 타는 보트의 수
            answer += 1
        e -= 1
    # 모든 사람이 구명보트를 하나씩 타는 최대값 - 2명이 같이 탄 구명보트의 수
    return len(people) - answer