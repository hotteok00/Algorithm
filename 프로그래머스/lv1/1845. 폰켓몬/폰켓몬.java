import java.util.*;
class Solution {
    public int solution(int[] nums) {
        int answer = 0;
        
        int N = nums.length;
        int n = N/2;
        Set<Integer> s = new HashSet<>();
        for(int i=0; i<N; i++)
            s.add(nums[i]);
        
        return (n < s.size()) ? n : s.size();
    }
}