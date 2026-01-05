class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        history = defaultdict(lambda: defaultdict(set))
        invalid = []

        for trans in transactions:
            name, time, amt, city = trans.split(",")
            time, amt = int(time), int(amt)

            history[time][name].add(city)

        for trans in transactions:
            name, time, amt, city = trans.split(",")
            time, amt = int(time), int(amt)
            
            if amt > 1000:
                invalid.append(trans)
                continue

            for t in range(time - 60, time + 61):
                if t not in history or name not in history[t]:
                    continue

                if len(history[t][name]) > 1 or next(iter(history[t][name])) != city:
                    invalid.append(trans)
                    break

        return invalid
    