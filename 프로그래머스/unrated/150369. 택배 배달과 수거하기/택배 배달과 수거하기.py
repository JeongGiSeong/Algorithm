def solution(cap, n, deliveries, pickups):
    ans = 0
    # 가면서 택배 배달, 오면서 재활용 수거
    # 먼 곳부터 처리해야 거리가 줆
    
    # 배달, 수거할 게 없는 경우
    while deliveries and deliveries[-1] == 0:
        deliveries.pop()
    while pickups and pickups[-1] == 0:
        pickups.pop()
    
    while deliveries or pickups:
        dist = 0 # 이번에 이동할 거리(편도)
        
        if deliveries:
            tmp = 0 # 이번에 배달할 택배의 개수
            dist = max(dist, len(deliveries)) # deliveries와 pickups 중 더 긴 리스트의 길이를 dist로 설정
            while tmp < cap and deliveries:
                if tmp + deliveries[-1] <= cap:
                    tmp += deliveries[-1]
                    deliveries.pop()
                else:
                    deliveries[-1] -= (cap - tmp)
                    tmp = cap
                    
        if pickups:
            tmp = 0 # 이번에 수거할 재활용의 개수
            dist = max(dist, len(pickups)) # deliveries와 pickups 중 더 긴 리스트의 길이를 dist로 설정
            while tmp < cap and pickups:
                if tmp + pickups[-1] <= cap:
                    tmp += pickups[-1]
                    pickups.pop()
                else:
                    pickups[-1] -= (cap - tmp)
                    tmp = cap
            
        ans += dist * 2
        
        # 배달, 수거할 게 없는 경우
        while deliveries and deliveries[-1] == 0:
            deliveries.pop()
        while pickups and pickups[-1] == 0:
            pickups.pop()
        
        # print(ans, deliveries, pickups)
        
    return ans