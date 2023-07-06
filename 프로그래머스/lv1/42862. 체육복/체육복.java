class Solution {
    public int solution(int n, int[] lost, int[] reserve) {
        int answer = 0;

        int[] all = new int[n + 1];
        for(int i=0; i<n+1; i++) all[i] = 1;
        
        for(int i : reserve) all[i] = 2;
        for(int i : lost) all[i] -= 1;
        
        for(int i=1; i<n+1; i++) {
            if(all[i] == 0) {
                if(i > 1 && all[i - 1] == 2) {
                    all[i] = 1;
                    all[i - 1] = 1;
                }
                else if (i < n && all[i + 1] == 2) {
                    all[i] = 1;
                    all[i + 1] = 1;
                }
            } 
        }
        
        for(int i=1; i<n+1; i++) if (all[i] > 0) answer++;
        
        
        
        return answer;
    }
}