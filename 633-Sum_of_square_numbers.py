#633. Sum of square numbers 

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(sqrt(c))

        while right>=left:
            if right*right+left*left == c:
                return True
            if right*right+left*left < c:
                left+=1
            else:
                right-=1
        return False
