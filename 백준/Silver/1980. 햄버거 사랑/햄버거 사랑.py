n, m, t = map(int, input().split())

max_burger = 0
min_coke = t

for i in range(t // n + 1):
    for j in range(t // m + 1):
        total_time = n * i + m * j
        if total_time <= t:
            coke_time = t - total_time
            # 남은 시간이 더 적은 경우 OR 시간이 같다면, 더 많은 햄버거를 먹은 경우
            if coke_time < min_coke or (coke_time == min_coke and i + j > max_burger):
                max_burger = i + j
                min_coke = coke_time

print(max_burger, min_coke)
