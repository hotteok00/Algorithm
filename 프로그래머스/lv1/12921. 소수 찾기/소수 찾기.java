import java.util.ArrayList;
class Solution {
    public int solution(int n) {
        int answer = 0;
        
        boolean[] arr = new boolean[n + 1];
        for(int i = 2; i < n+1; i++) {
            if(!arr[i]) {
                answer++;
                for(int j = 2*i; j < n+1; j+=i) arr[j] = true;
            }
        }
        
        return answer;
    }
}