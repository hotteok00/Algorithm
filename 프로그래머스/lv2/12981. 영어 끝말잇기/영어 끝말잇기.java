import java.util.Set;
import java.util.HashSet;

class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];

        int idx = 0, cnt = 0;
        Set<String> set = new HashSet<>();
        
        for(int i = 0; idx < words.length; i = ++i % n, idx++) {
            if(i == 0) cnt++;
            if(idx == 0) {
                set.add(words[idx]);
                continue;
            }
            if(set.contains(words[idx]) || words[idx].charAt(0) != words[idx-1].charAt(words[idx-1].length() - 1)) {
                answer[0] = ++i;
                answer[1] = cnt;
                break;
            }
            else set.add(words[idx]);
        }

        return answer;
    }
}