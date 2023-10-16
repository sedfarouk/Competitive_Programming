class Solution {
    public int reverse(int x) {
        double ans = 0;
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

        if (isNeg){
            ans *= -1;
        }

        if (ans > Math.pow(2, 31) || ans < -(Math.pow(2, 31))){
            return 0;
        } 

        return (int)(ans);
    }
}