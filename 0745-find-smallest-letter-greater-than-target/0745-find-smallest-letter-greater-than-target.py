class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        left, right = 0, len(letters) - 1
        greater = letters[0]

        while left <= right:
            mid = left + (right-left) // 2

            if ord(letters[mid]) > ord(target):
                right = mid - 1
                greater = letters[mid]
            else:
                left = mid + 1
        return greater
             

