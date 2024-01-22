class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.board = []
        hashmap = defaultdict(int)
        maxx = -1

        for i in range(len(self.times)):
            hashmap[self.persons[i]] += 1

            if hashmap[self.persons[i]] >= maxx:
                self.board.append(persons[i])
                maxx = hashmap[self.persons[i]]
            else:
                self.board.append(self.board[-1])

    def q(self, t: int) -> int:
        l, r = -1, len(self.times)
        ans = 0
        
        while l + 1 < r:
            m = l + (r-l)//2

            if self.times[m] <= t:
                l = m
            else:
                r = m
                
        return self.board[l]
            


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)