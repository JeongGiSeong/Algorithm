class Solution:
    def robotWithString(self, s: str) -> str:
        t = []
        result = []
        cnt = Counter(s)
        
        for ch in s:
            t.append(ch)

            if cnt[ch] == 1:
                del cnt[ch]
            else:
                cnt[ch] -= 1

            while cnt and t and min(cnt)>=t[-1]:
                result += t.pop()

            
        result += t[::-1]
        return ''.join(result)