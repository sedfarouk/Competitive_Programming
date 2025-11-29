class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        n = len(transactions)
        parsed = []

        for idx, transaction in enumerate(transactions):
            name, time, amt, city = transaction.split(",")
            parsed.append((name, int(time), int(amt), city, idx))

        parsed.sort(key = lambda x: x[1])
        city_trans = defaultdict(lambda: defaultdict(deque))
        invalid = [False] * n

        for name, time, amt, city, idx in parsed:
            if amt > 1000:
                invalid[idx] = True

            for other_city, name_maps in city_trans.items():
                if other_city == city:
                    continue

                dq = name_maps[name]

                while dq and time - dq[0][0] > 60:
                    dq.popleft()

                if dq: invalid[idx] = True

                for time2, idx2 in dq:
                    invalid[idx2] = True

            city_trans[city][name].append((time, idx))

        return [transactions[x] for x in range(n) if invalid[x]]

