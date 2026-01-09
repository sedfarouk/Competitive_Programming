class Solution:
    def isHappy(self, n: int) -> bool:
        # tortoise-hare (Floyd) algorithm
        def findHappyNum(x):
            res = 0
            while x:
                res += (x % 10) ** 2
                x //= 10
            return res

        slow, fast = n, findHappyNum(n)
        while fast != 1 and slow != fast:
            slow = findHappyNum(slow)
            fast = findHappyNum(findHappyNum(fast))

        return fast == 1