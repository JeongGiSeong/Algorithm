from bisect import bisect_left, bisect_right

N = int(input())
hav = sorted(list(map(int, input().split())))
M = int(input())
cards = list(map(int, input().split()))

ans = []
for card in cards:
    l = bisect_left(hav, card)
    r = bisect_right(hav, card)
    ans.append(1 if r - l > 0 else 0)

print(*ans)