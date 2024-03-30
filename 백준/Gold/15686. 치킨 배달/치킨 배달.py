import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
houses = []
chickens = []

# N(2 ≤ N ≤ 50), M(1 ≤ M ≤ 13)
# 치킨 집이 최대 13개. 13 C 7 = 1716
# 집은 최대 100개. 100 * 7(치킨집 수) * 1716 = 약 120만
# 즉, 완전탐색으로 돌려도 시간 내에 가능

for i in range(N):
    for j, v in enumerate(map(int, input().split())):
        if v == 1:
            houses.append((i, j))
        elif v == 2:
            chickens.append((i, j))

def get_dist(a, b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

ans = float('inf')
for combi in combinations(chickens, M):
    total = 0 # 도시의 치킨 거리
    for house in houses:
        total += min(get_dist(house, chicken) for chicken in combi)
    # print(f'combi: {combi} | total: {total}')
    ans = min(ans, total)
print(ans)