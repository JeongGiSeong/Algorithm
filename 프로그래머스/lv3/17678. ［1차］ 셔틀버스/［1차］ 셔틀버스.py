def hourToMinute(time):
    h, m = map(int, time.split(':'))
    return h * 60 + m

def minuteToHour(minute):
    h = minute // 60
    m = minute % 60
    return f"{str(h).zfill(2)}:{str(m).zfill(2)}"

def solution(n, t, m, timetable):
    crewTime = sorted([hourToMinute(time) for time in timetable])
    busTime = [hourToMinute("09:00") + t*i for i in range(n)]
    
    last_person_time = 0
    idx_crew = 0 # 다음에 탑승할 크루의 인덱스
    
    for bus in busTime:
        count = 0 # 버스에 탑승한 크루의 수
        
        # 조건1: 버스에 자리가 있고,
        # 조건2: 아직 탑승하지 않은 크루가 남아있으며,
        # 조건3: 대기 중인 크루가 버스 도착 시간 이전 또는 동시에 도착하면 
        while count < m and idx_crew < len(crewTime) and crewTime[idx_crew] <= bus:
            idx_crew += 1
            count += 1
        
        if count < m: 
            # 만약 현재 버스에 자리가 남았다면,
            last_person_time = bus
        else:
            # 만약 현재 버스가 가득 찼다면,
            last_person_time = crewTime[idx_crew - 1] - 1

    return minuteToHour(last_person_time)
