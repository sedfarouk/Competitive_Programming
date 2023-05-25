class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        commonPrefix = ""
        strs = sorted(strs)   
        firstWord = strs[0]   
        lastWord = strs[-1]

        for i in range(min(len(firstWord), len(lastWord))):
            if (firstWord[i] != lastWord[i]):
                return commonPrefix
            commonPrefix+=firstWord[i]
        return commonPrefix
    
    
    
obj = Solution
print(obj.longestCommonPrefix(obj,strs=["Hello", "Hey", "Henok"]))