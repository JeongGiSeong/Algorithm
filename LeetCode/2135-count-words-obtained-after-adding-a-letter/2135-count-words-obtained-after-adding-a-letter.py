# startword: [g, j], targetword: [jg] 이걸 1번으로 쳐야된다는건가?
class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        startWordSet = set(''.join(sorted(word)) for word in startWords)
        targetWordSet = set(''.join(sorted(word)) for word in targetWords)
        count = 0

        for targetWord in targetWordSet:
            for i in range(len(targetWord)):
                # targetWord에서 1개를 뺀 문자열이 startWordSet에 있는지 확인
                modifiedTarget = targetWord[:i] + targetWord[i+1:]
                if modifiedTarget in startWordSet:
                    count += 1
                    break

        return count
        
        
################# 시간 초과 ##################  
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