import sys

input = sys.stdin.readline

top, bottom = 10 ** 18 + 1, -10 ** 18 -1
string = "Hmm..."
ans = 0
for i in range(int(input())):
    n, updown = input().split()
    n = int(n)

    if updown == '^':
        bottom = max(bottom, n)
    else:
        top = min(top, n)

    diff = top - bottom
    if diff < 2:
        string = "Paradox!"
        ans = i+1
        break
    elif diff == 2 and ans == 0:
        string = "I got it!"
        ans = i+1

print(string)
if ans > 0:
    print(ans)


######### 오답노트 ########
# 1. 정답을 찾았다고 끝나는 게 아니라, 이후에도 모순이 있다면 패러독스가 출력되어야 함
# 2. 범위 설정을 float('inf')로 했더니 아래 반례에서 틀림

# 1
# 999999999999999999 ^
# 정답: "I got it!"
#       1
# 출력: "Hmm..."
