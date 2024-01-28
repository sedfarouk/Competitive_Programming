/**
 * @param {number[]} nums
 * @param {number} left
 * @param {number} right
 * @return {number}
 */
var numSubarrayBoundedMax = function(nums, left, right) {
    let l = r = -1;
    let ans = 0;
    
    for (let i=0; i < nums.length; i++){
        if (nums[i] >= left) r = i;
        if (nums[i] > right) l = r = i;
        ans += r-l;
    }
    
    return ans;
};
