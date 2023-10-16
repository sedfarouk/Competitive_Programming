class Solution {
    public int reverse(int x) {
        long ans = 0;
        Boolean isNeg = false;

        if (x < 0){
            isNeg = true;
            x *= -1;
        }

        while (x > 0){
            int rem = x % 10;
            x /= 10;
            ans = ans*10 + rem;
        }

        if (ans > Integer.MAX_VALUE){
            return 0;
        }

        return (int) (isNeg ? -ans : ans);
    }
}