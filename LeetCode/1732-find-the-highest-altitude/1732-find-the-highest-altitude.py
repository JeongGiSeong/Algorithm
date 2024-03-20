class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = altitude = 0

        for i in gain:
            highest = max(highest, altitude + i)
            altitude += i

        return highest