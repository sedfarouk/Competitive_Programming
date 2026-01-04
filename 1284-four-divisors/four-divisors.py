class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        ans = 0

        def countDivs(x):
            divs = []
            for i in range(1, int(x ** 0.5) + 1):
                if x % i == 0:
                    divs.append(i)

                    if (x // i) != i:
                        divs.append(x // i)

                if len(divs) > 4:
                    return 0
            return sum(divs) if len(divs) == 4 else 0

        for num in nums:
            ans += countDivs(num)

        return ans
