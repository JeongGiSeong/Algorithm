heights = [int(input()) for _ in range(9)]
heights.sort()
total = sum(heights)

def f():
    for i in range(8):
        for j in range(i+1, 9):
            if total - heights[i] - heights[j] == 100:
                for k in range(9):
                    if i !=k and j !=k:
                        print(heights[k])

                return

f()