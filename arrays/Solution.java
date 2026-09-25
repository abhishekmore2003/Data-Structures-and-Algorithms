import java.util.*;

public class Solution {
    public int missingNumber(int[] nums) {

        int expectedsum = nums.length * (nums.length + 1) / 2 ;
        int actualsum = 0;
        for (int i : nums)
        {
            actualsum += i ;
        }

        return expectedsum - actualsum;
    }


    public static void main(String[]args)
    {
        int array[] = {9,6,4,2,3,5,7,0,1};
        Solution obj = new Solution();
        System.out.println(obj.missingNumber(array));
    }
}