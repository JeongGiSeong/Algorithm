import heapq, sys
input = sys.stdin.readline

# 멜로디에 포함되어 있는 음의 수 N과 한 줄에 있는 프렛의 수 P
# (1 ≤ N ≤ 500,000, 2 ≤ P ≤ 300,000)
N, P = map(int, input().split())
strings = [[] for _ in range(7)]
ans = 0

# 만약, 어떤 줄의 프렛을 여러 개 누르고 있다면, 가장 높은 프렛의 음이 발생한다.

for _ in range(N):
    s, p = map(int, input().split())
    while strings[s] and strings[s][-1] > p:
        strings[s].pop()
        ans += 1
    
    if strings[s] and strings[s][-1] == p:
        continue

    strings[s].append(p)
    ans += 1
    # for i in range(1,7):
    #     print(f's[{i}]:{strings[i]}, ans:{ans}')

print(ans)