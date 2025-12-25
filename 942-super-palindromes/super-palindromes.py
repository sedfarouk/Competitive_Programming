class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left, right = int(left), int(right)
        l, r = int(left ** 0.5), int(right** 0.5)
        ans = 0

        def isSuperPalindrome(num):
            sq_num = str(int(num) ** 2)

            if left <= int(sq_num) <= right and sq_num == sq_num[::-1]:
                return True
            return False

        for i in range(10 ** 5):
            num = str(i)
            num1, num2 = num + num[:-1][::-1], num + num[::-1]

            ans += int(isSuperPalindrome(num1))
            ans += int(isSuperPalindrome(num2))

        return ans
            
