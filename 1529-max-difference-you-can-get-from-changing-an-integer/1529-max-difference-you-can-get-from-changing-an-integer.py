class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)

        def convert(digit):
            ptr = 0
            new_num = []

            while ptr < len(num_str) and num_str[ptr] == digit:
                new_num.append(num_str[ptr])
                ptr += 1

            j = ptr
            if j > 0 and digit == '1': 
                digit = '0'
                while ptr < len(num_str) and num_str[ptr] in ('0', '1'):
                    new_num.append(num_str[ptr])
                    ptr += 1
                j = ptr
                
            while ptr < len(num_str):
                new_num.append(digit if num_str[ptr] == num_str[j] else num_str[ptr])
                ptr += 1

            return int("".join(new_num))

        return convert('9') - convert('1')

        
    


