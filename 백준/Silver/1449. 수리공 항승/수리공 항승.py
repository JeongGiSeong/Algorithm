import sys
input = sys.stdin.readline

N, L = map(int, input().split())
pipes = list(map(int, input().split()))
pipes.sort()

ans = 1
cur = pipes[0]
for pipe in pipes:
    if pipe >= cur + L:
        ans += 1
        cur = pipe

print(ans)