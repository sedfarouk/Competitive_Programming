class Solution:
    def bestClosingTime(self, customers: str) -> int:
        pf_sum, sf_sum = [0], [0]

        for i in range(len(customers)):
            if customers[i]=="N":
                pf_sum.append(pf_sum[-1]+1)
            else:
                pf_sum.append(pf_sum[-1])

        for i in range(len(customers)-1, -1, -1):
            if customers[i]=="Y":
                sf_sum.append(sf_sum[-1]+1)
            else:
                sf_sum.append(sf_sum[-1])
        
        sf_sum.reverse()

        penalty = float("inf")
        pos = 0
        for i in range(len(pf_sum)):
            x = pf_sum[i] + sf_sum[i]
            
            if x < penalty:
                penalty = x
                pos = i

        return pos
