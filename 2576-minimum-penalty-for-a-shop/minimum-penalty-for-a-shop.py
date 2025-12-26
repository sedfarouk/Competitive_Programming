class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)
        ans = -1
        score = maxScore = 0

        for i in range(n):
            if customers[i] == 'Y': score += 1
            else: score -= 1

            if score > maxScore:
                ans = i 
                maxScore = score

        return ans + 1