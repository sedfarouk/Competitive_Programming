class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        ans, window = 0, sum(arr[left:k])

        for right in range(k,len(arr)):
            avg = window / k
            
            if avg >= threshold:
                ans += 1
            
            window += arr[right]
            window -= arr[left]
            left += 1

        if window/k >= threshold:
            ans += 1
        return ans

            
