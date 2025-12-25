class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        left, right = int(left), int(right)
        ans = 0

        def isPalindrome(x):
            return x == x[::-1]

        for i in range(10 ** 5):
            num = str(i)
            num = num + num[:-1][::-1]
            sq_num = int(num) ** 2

            if sq_num > right:
                break

            ans += int(sq_num >= left and isPalindrome(str(sq_num)))

        for i in range(10 ** 5):
            num = str(i)
            num = num + num[::-1]
            sq_num = int(num) ** 2

            if sq_num > right:
                break

            ans += int(sq_num >= left and isPalindrome(str(sq_num)))

        return ans
            
