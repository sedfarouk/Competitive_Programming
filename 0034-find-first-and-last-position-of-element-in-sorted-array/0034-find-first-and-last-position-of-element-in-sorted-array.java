class Solution {
    public int[] searchRange(int[] nums, int target) {
        int left = 0;
        int right = nums.length-1;
        int start, end = -1;

        while (left <= right){
            int mid = left + (right - left) / 2;

            if (nums[mid] >= target){
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        start = left;

        left = 0;
        right = nums.length-1;

        while (left <= right){
            int mid = left + (right - left) / 2;

            if (nums[mid] <= target){
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        end = right;

        if (start > end || start == -1 || end == -1){
            return new int[] {-1, -1};
        }

        return new int[] {start, end};
    }
}