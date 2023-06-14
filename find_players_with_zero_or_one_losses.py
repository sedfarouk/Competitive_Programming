class Solution:
    def findWinners(self, matches: list[list[int]]) -> list[list[int]]:
        winner_records = {}
        loser_records = {}

        for winner,loser in matches:
            winner_records[winner] = winner_records.get(winner,0) + 1
            loser_records[loser] = loser_records.get(loser,0) + 1
            
        w = [i for i in winner_records if i not in loser_records]
        l = [j for j in loser_records if loser_records[j]==1]

        answer = [sorted(w),sorted(l)]

        return answer