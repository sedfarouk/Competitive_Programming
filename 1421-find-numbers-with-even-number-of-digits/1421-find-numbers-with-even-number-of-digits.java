class Solution {
    public int findNumbers(int[] nums) {
        int ans = 0;

        for (int num : nums){
            if (num < 0){
            num *= -1;
            }
            int len = (int)(Math.log10(num) + 1);

            if (len % 2 == 0){
                ans++;
            }
        }

        return ans;
        }
    }