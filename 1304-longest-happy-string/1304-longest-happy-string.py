class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        ans = []
        mx = max(a, b, c)
        abc = ['a', 'b', 'c']
        cnt = [a, b, c]
        ptr = 0

        if mx==b: ptr = 1
        elif mx==c: ptr = 2   

        while cnt[ptr] > 0:
            ans.append(abc[ptr])
            cnt[ptr] -= 1

            if cnt[ptr] > 0 and ans[-2:] != [abc[ptr], abc[ptr]]:
                ans.append(abc[ptr])
                cnt[ptr] -= 1

            for i in range(3):
                if i != ptr and cnt[i] > 0:
                    ans.append(abc[i])
                    cnt[i] -= 1
                    break

            mx = max(cnt[0], cnt[1], cnt[2])
            if mx==cnt[0] and ans[-2:] != [abc[0], abc[0]]:
                ptr = 0
            elif mx==cnt[1] and ans[-2:] != [abc[1], abc[1]]:
                ptr = 1
            elif mx==cnt[2] and ans[-2:] != [abc[2], abc[2]]:
                ptr = 2
            else:
                break

        return "".join(ans)

            
