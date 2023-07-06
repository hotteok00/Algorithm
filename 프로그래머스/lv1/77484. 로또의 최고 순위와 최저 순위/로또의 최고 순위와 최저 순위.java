import java.util.Arrays;
class Solution {
    public int[] solution(int[] lottos, int[] win_nums) {
        int[] answer = {6, 6};
        
        Arrays.sort(lottos);
        Arrays.sort(win_nums);
        
        for(int i = 5; i >= 0; i--) {
            for(int j = 5; j >= 0; j--) {
                if(lottos[i] == win_nums[j]) {
                    answer[0]--; 
                    answer[1]--;
                }
            }
        }
        
        for(int i = 5; i >= 0; i--)
            if(lottos[i] == 0) answer[0]--;
            
        answer[0] = (answer[0] != 6) ? (answer[0] + 1) : 6;
        answer[1] = (answer[1] != 6) ? (answer[1] + 1) : 6;
        return answer;
    }
}