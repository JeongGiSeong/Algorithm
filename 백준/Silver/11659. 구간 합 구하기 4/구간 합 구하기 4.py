import sys
input = sys.stdin.readline

# Prefix Sum
N, M = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(1, N):
    nums[i] = nums[i-1] + nums[i]
nums.insert(0, 0)

for i in range(M):
    s, e = map(int, input().split())
    print(nums[e] - nums[s-1])