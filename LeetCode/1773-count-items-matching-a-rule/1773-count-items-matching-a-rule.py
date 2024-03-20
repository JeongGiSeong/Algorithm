class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        answer = 0
        key = {'type':0, 'color':1, 'name':2}

        for item in items:
            if item[key[ruleKey]] == ruleValue:
                answer += 1

        return answer