class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)

        stk = [defaultdict(int)]
        i = 0

        while i < n:
            curr = ''

            if formula[i] == '(':
                stk.append(defaultdict(int))
                i += 1

            while i < n and formula[i].isalpha():
                if curr and formula[i].isupper():
                    break
                curr += formula[i]
                i += 1

            pop = False
            if i < n and formula[i] == ')':
                pop = True
                i += 1

            cnt = 0
            while i < n and formula[i].isdigit():
                cnt = (cnt * 10) + int(formula[i])
                i += 1
            cnt = max(1, cnt)

            if pop:
                col = stk.pop()
                for k, v in col.items():
                    stk[-1][k] += v * cnt
            if curr: stk[-1][curr] += cnt

        ans = ''
        for k in sorted(list(stk[-1].keys())):
            ans += k + (str(stk[-1][k]) if stk[-1][k] > 1 else '')

        return ans


        