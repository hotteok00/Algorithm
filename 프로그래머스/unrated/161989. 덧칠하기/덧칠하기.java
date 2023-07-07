class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        
        int idx = 0;
        for(int i=0; i < section.length; i++) {
            if (idx > n) break;
            if (idx > section[i]) continue;
            idx = section[i];
            idx += m;
            answer++;
        }
        
        // int idx=0;
        // int[] completed = new int[n+1];
        // for(int i=1; i<n+1 - n; i++) {
        //     if(i == section[idx]) {
        //         i += m-1;
        //         answer++;
        //         idx++;
        //     }
        //     if (i > section[idx]) idx++;
        // }
        
        return answer;
    }
}