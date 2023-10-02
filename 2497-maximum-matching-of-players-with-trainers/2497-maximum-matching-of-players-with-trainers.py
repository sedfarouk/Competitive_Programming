class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        ans = 0
        trainers.sort()
        players.sort()

        p_pointer, t_pointer = 0, 0
        
        while p_pointer < len(players) and t_pointer < len(trainers):
            if players[p_pointer] <= trainers[t_pointer]:
                ans+=1
                p_pointer+=1
            t_pointer+=1
        return ans