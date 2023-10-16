class Solution {
    public int maxArea(int[] height) {
        int left = 0;
        int right = height.length-1;
        int ans = 0;

        while (left <= right){
            if (height[left] < height[right]){
                ans = Math.max(ans, (right-left) * height[left]);
                left++;
            }
            else if (height[left] > height[right]){
                ans = Math.max(ans, (right-left) * height[right]);
                right--;
            }
            else{
                ans = Math.max(ans, (right-left) * height[left]);
                left++;
                right--;
            }
        }

        return ans;
    }
}