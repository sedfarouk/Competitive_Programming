class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int maxx = Integer.MIN_VALUE;

        List<Boolean> ans = new ArrayList<>();

        for (int num : candies){
            maxx = Math.max(maxx, num);
        }

        for (int num : candies){
            if (num + extraCandies >= maxx){
                ans.add(true);
            } else {
                ans.add(false);
            }
        }

        return ans;
    }
}