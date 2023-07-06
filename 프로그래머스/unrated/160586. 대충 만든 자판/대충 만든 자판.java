import java.util.HashMap;

class Solution {
    public int[] solution(String[] keymap, String[] targets) {
        int[] answer = new int[targets.length];
        
        HashMap<Character, Integer> hm = new HashMap<>();
        for(String s : keymap)
            for(int i=0; i<s.length(); i++) {
                char c = s.charAt(i);
                if (hm.containsKey(c)) 
                    hm.put(c, Math.min(hm.get(c), i));
                else 
                    hm.put(c, i);
            }
        
        for(int i=0; i<targets.length; i++) {
            String s = targets[i];
            for(int j=0; j<s.length(); j++) {
                char c = s.charAt(j);
                if(hm.containsKey(c)) 
                    answer[i] += hm.get(c) + 1;
                else {
                    answer[i] = -1;
                    break;
                }
            }
        }
        
        return answer;
    }
}