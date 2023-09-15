class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = -1, len(letters)

        while left + 1 < right:
            mid = left + (right - left) // 2

            if letters[mid] <= target:
                left = mid
            else:
                right = mid 
        
        if right >= len(letters):
            return letters[0]
        return letters[right]





        


        



                         

