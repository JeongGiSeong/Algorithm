import sys

read = sys.stdin.readline



# 2xn 타일링, 1초, 메모리 256
# 2xn 크기의 직사각형을 1x2, 2x1 타일로 채우는 방법의 수를 구하라
# 첫째줄 n(1~1000)
# 방법의 수를 10007로 나눈 나머지 출력하라

# 규칙이 피보나치 수열
n = int(read())
s = [0, 1, 2]
for i in range(3, n + 1):
  s.append(s[i - 2] + s[i - 1])
print(s[n] % 10007)