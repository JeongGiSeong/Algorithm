import sys
input = sys.stdin.readline

N = int(input())
req = list(map(int, input().split()))
M = int(input())

low = 0
high = max(req)
mid = (low + high) // 2
ans = 0

def is_possible(mid):
    return sum(min(r, mid) for r in req) <= M


while low <= high:
    # print(f'low:{low}, mid:{mid}, high:{high}, ans:{ans}')
    if is_possible(mid):
        low = mid + 1
        ans = mid
    else:
        high = mid - 1

    mid = (low + high) // 2

print(ans)