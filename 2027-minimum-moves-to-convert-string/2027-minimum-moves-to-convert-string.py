# move : '연속된 3 글자를 'O'로 변환
# s의 문자가 전부 'O'가 되려면 몇 번의 move를 해야 하는가?
class Solution:
    def minimumMoves(self, s: str) -> int:
        ans = i = 0
        while i < len(s): 
            if s[i] == "X": 
                ans += 1
                i += 3
            else: i += 1
        return ans