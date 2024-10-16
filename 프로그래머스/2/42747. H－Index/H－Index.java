import java.util.Arrays;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations);
        int n = citations.length;
        int h = 0;
        
        for (int i = 0; i < n; i++) {
            int smaller = Math.min(citations[i], n - i);
            h = Math.max(h, smaller);
        }
        
        return h;
    }
}