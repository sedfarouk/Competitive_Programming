class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int maxx = Arrays.stream(candies).max().getAsInt();
        ArrayList<Boolean> ans = new ArrayList<Boolean>();

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