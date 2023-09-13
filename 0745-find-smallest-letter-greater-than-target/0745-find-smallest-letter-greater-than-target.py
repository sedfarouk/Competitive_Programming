class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, mid, right = 0, 0, len(letters)-1

        while left <= right:
            mid = left + (right - left)//2

            if ord(letters[mid]) > ord(target):
                right = mid - 1
            elif ord(letters[mid]) < ord(target):
                left = mid + 1
            else:
                for i in range(mid+1, len(letters)):
                    if ord(letters[i]) > ord(target):
                        return letters[i]   
                break
        
        for j in range(len(letters)):
            if ord(letters[j]) > ord(target):
                return letters[j]
        return letters[0]

