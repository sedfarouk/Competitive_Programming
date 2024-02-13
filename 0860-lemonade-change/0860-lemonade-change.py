class Solution:
    def lemonadeChange(self, costs: List[int]) -> bool:
        bills = {5:0, 10:0, 20:0}
        
        for b in costs:
            if b==10:
                if bills[5]==0:
                    return False
                bills[5] -= 1
            if b==20:
                if bills[10]==0:
                    if bills[5]<3:
                        return False
                    bills[5]-=3
                if bills[10]>0:
                    if bills[5]==0:
                        return False
                    bills[5]-=1; bills[10]-=1
            bills[b] += 1

        return True
        