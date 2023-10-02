class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        n = len(colors)
        Alice_picks = Bob_picks = 0

        if n <= 2:
            return False

        for i in range(1, n-1):
            if colors[i]=='A' and colors[i-1]=='A' and colors[i+1]=='A':
                Alice_picks += 1
            if colors[i]=='B' and colors[i-1]=='B' and colors[i+1]=='B':
                Bob_picks += 1

        if Alice_picks > Bob_picks:
            return True
        return False