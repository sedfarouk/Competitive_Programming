class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans, cnt = 0, 0
        hashmap = defaultdict(int)
        left = 0

        for right in range(len(fruits)):
            hashmap[fruits[right]]+=1

            while len(hashmap.keys())==3:
                ans = max(ans, right-left)
                if hashmap[fruits[left]] > 1:
                    hashmap[fruits[left]]-=1
                else:
                    del hashmap[fruits[left]]
                left+=1
        ans = max(ans, right-left+1)

        return ans

            