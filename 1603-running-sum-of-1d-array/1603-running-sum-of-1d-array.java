class Solution {
    public int[] runningSum(int[] nums) {
        int[] ans = new int[nums.length];
        int running_sum = 0;

        for (int i=0; i < nums.length; i++){
            running_sum += nums[i];
            ans[i] = running_sum;
        }

        return ans;
    }
}