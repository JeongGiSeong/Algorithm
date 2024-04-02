# 1, 1, 1, 2, 2, 3, 4, 5, 7, 9
# padovan[i] = padovan[i-2] + padovan[i-3]
import sys
input = sys.stdin.readline

padovan = [0] * 101

padovan[1], padovan[2], padovan[3] = 1, 1, 1
for i in range(4, 101):
    padovan[i] = padovan[i-2] + padovan[i-3]

for _ in range(int(input())):
    print(padovan[int(input())])