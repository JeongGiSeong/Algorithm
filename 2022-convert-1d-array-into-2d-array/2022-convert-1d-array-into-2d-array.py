class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []

        new = []
        for i in range(m):
            temp = original[m*i:m*i+n]
            new.append(temp)

        return new