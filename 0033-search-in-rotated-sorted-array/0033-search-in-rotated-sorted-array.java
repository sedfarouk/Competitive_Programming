class Solution {
    public int search(int[] nums, int target) {
        int pivot = findPivot(nums);

        int left = 0;
        int right = pivot;

        while (left <= right){
            int mid = left + (right - left) / 2;

            if (nums[mid]==target){
                return mid;
            } else if (nums[mid] > target){
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        left = pivot + 1;
        right = nums.length-1;

        while (left <= right){
            int mid = left + (right - left) / 2;

            if (nums[mid]==target){
                return mid;
            } else if (nums[mid] > target){
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }

        return -1;
    }

    private int findPivot(int[] nums){
        int left = 0;
        int right = nums.length-1;

        while (left <= right){
            int mid = left + (right - left) / 2;

            if (mid < right && nums[mid] > nums[mid+1]){
                return mid;
            }

            if (mid > left && nums[mid] < nums[mid-1]){
                return mid - 1;
            }

            if (nums[mid] > nums[left]){
                left = mid;
            } else {
                right = mid-1;
            }
        }

        return -1;
    }
}