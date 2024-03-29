import sys
input = sys.stdin.readline

cnt = 0
while True:
    cnt += 1
    L, P, V = map(int, input().split())
    if L == P == V == 0:
        break

    ans = (V // P) * L + min((V % P), L)
    print(f'Case {cnt}: {ans}')