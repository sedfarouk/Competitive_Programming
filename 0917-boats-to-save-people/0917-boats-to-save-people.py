class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        people.sort()
        right, left = len(people)-1, 0
        tmp = 0

        while left <= right:
            if people[left]+people[right] <= limit:
                left+=1
            right-=1
            ans+=1               

        return ans 

            

