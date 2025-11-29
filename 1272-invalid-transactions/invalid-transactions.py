from collections import defaultdict, deque
from typing import List

class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        n = len(transactions)
        parsed = []
        for i, t in enumerate(transactions):
            name, time, amt, city = t.split(',')
            parsed.append((name, int(time), int(amt), city, i))

        parsed.sort(key=lambda x: x[1])

        tr = defaultdict(lambda: defaultdict(deque))
        invalid = [False] * n  

        for name, time, amt, city, idx in parsed:
            if amt > 1000:
                invalid[idx] = True

            for other_city, name_map in tr.items():
                if other_city == city:
                    continue

                dq = name_map[name]
                while dq and time - dq[0][0] > 60:
                    dq.popleft()

                for t2, a2, idx2 in dq:
                    invalid[idx2] = True
                    invalid[idx] = True

            tr[city][name].append((time, amt, idx))

        return [transactions[i] for i in range(n) if invalid[i]]
