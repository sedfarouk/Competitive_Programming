class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int i = 0;
        int x = 0;

        while (i < operations.length){
            if (operations[i].charAt(1) == '+'){
                x+=1;
            }
            else{
                x-=1;
            }
                
            i++;
            }

        return x;
        }
    }
