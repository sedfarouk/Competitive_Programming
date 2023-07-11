class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        first, last = 0, len(numbers)-1
        while first<len(numbers) and last>0:
            num = numbers[first]+numbers[last]
            if num==target:
                return [first+1,last+1]
            elif num<target:
                first+=1
            else:
                last-=1