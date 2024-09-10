# 1. 문자열에 없는 소문자를 끝에 추가
# 2. 문자열을 임의의 순서로 재배열한다
# 주어지는 문자열에는 중복되는 문자가 없음

# 1. startword의 모든 문자가 targetword에 있어야 함
# 2. startword의 길이는 targetword의 길이에 1을 뺀 값
# startword: [g, j], targetword: [jg] 이걸 1번으로 쳐야된다는건가?
        
# class Solution:
#     def check(self, startWord: str, targetWord: str)-> bool:
#         if len(startWord) != len(targetWord)-1:
#             return False
#         for s in startWord:
#             if s not in targetWord:
#                 return False
#         return True


#     def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
#         ans = 0
#         targetWords.sort()
#         startWords.sort()
#         for targetWord in targetWords:
#             for startWord in startWords:
#                 if self.check(startWord, targetWord):
#                     ans += 1 
#                     break

#         return ans

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        startWordSet = set(''.join(sorted(word)) for word in startWords)
        count = 0

        for targetWord in targetWords:
            sortedTarget = ''.join(sorted(targetWord))
            for i in range(len(sortedTarget)):
                modifiedTarget = sortedTarget[:i] + sortedTarget[i+1:]
                if modifiedTarget in startWordSet:
                    count += 1
                    break

        return count