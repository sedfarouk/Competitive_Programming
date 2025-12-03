class Solution:
    def intToRoman(self, num: int) -> str:
        roman = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        ans = []

        i = 0
        while num:
            last_digit = num % 10

            if i == 3:
                ans.append(last_digit * 'M')
                break
            
            if last_digit == 4 or last_digit == 9:
                if last_digit == 4:
                    val = roman[10**i] + roman[5*10**i]
                else:
                    val = roman[10**i] + roman[10**(i+1)]
            else:
                val = (roman[5*(10**i)] if last_digit >= 5 else '') + roman[10**i] * (last_digit % 5)

            ans.append(val)
            num //= 10
            i += 1

        return "".join(reversed(ans))


