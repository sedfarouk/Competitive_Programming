# 2657. Leetcode - Find the prefix common array of two arrays 

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        hashmap_A, hashmap_B = defaultdict(int), defaultdict(int)
        prefix_sum = [0]
        pointer = 0

        while pointer < len(A):
            hashmap_A[A[pointer]]+=1
            hashmap_B[B[pointer]]+=1

            x = bool(hashmap_A.get(B[pointer])) + bool(hashmap_B.get(A[pointer], 0))
            if A[pointer]==B[pointer]:
                prefix_sum.append(prefix_sum[-1]+1)
            else:
                prefix_sum.append(prefix_sum[-1]+x)
        
            pointer+=1

        return prefix_sum[1:]
