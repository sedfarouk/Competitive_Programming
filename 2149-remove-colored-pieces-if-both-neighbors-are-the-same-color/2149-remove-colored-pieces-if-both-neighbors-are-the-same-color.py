class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        Alice_picks = Bob_picks = 0

        if n <= 2:
            return False

        for i in range(1, n-1):
            if colors[i]==colors[i-1] and colors[i]==colors[i+1]:
                if colors[i]=='A':
                    Alice_picks += 1
                else:
                    Bob_picks += 1

        return Alice_picks > Bob_picks