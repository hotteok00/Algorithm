import java.util.Arrays;

class Solution {
    public int[] solution(int[] array, int[][] commands) {
        int a = commands.length;
        int[] answer = new int[a];
        
        int[] tmp;
        int idx;
        for(int i=0; i<a; i++) {
            tmp = new int[commands[i][1] - (commands[i][0]-1)];
            idx=0;
            for(int j=commands[i][0]-1; j<commands[i][1]; j++, idx++)
                tmp[idx] = array[j];
            Arrays.sort(tmp);
            answer[i] = tmp[commands[i][2] - 1];
        }
        
        return answer;
    }
}