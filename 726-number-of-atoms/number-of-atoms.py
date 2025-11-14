class Solution:
    def countOfAtoms(self, formula: str) -> str:
        n = len(formula)

        stk = [defaultdict(int)]
        i = 0

        while i < n:
            curr = ''

            # START CALCULATING VALUES FOR THOSE IN CURRENT BRACKET
            if formula[i] == '(':
                stk.append(defaultdict(int))
                i += 1

            # GET CURRENT ELEMENR
            while i < n and formula[i].isalpha():
                if curr and formula[i].isupper():
                    break
                curr += formula[i]
                i += 1

            # INDICATES IF WE ARE DONE CALCULATING FOR ALL ELEMENTS IN A BRACKET
            pop = False
            if i < n and formula[i] == ')':
                pop = True
                i += 1

            # GET CURRENT ELEMENT/BRACKET MULTIPLICATION FACTOR
            cnt = 0
            while i < n and formula[i].isdigit():
                cnt = (cnt * 10) + int(formula[i])
                i += 1
            cnt = max(1, cnt)

            # IF A BRACKET JUST GOT CLOSED THEN MULTIPLY EACH ELEMENT IN BRACKET WITH MULTIPLICATION FACTOR
            # AND INCREASE INITIAL VALUES OF SUCH ELEMENTS IN PREVIOUS BRACKET
            if pop:
                col = stk.pop()
                for k, v in col.items():
                    stk[-1][k] += v * cnt

            # ASSIGN CURRENT ELEMENT ITS MULTIPLICATION FACTOR
            if curr: stk[-1][curr] += cnt

        ans = ''
        for k in sorted(list(stk[-1].keys())):
            ans += k + (str(stk[-1][k]) if stk[-1][k] > 1 else '')

        return ans


        