import java.util.HashMap;

class Solution {
    public int[] solution(String s) {
        String[] str = s.split("");
        int[] answer = new int[str.length];
        
        HashMap<String, Integer> hm = new HashMap<>();
        for(int i=0; i<str.length; i++) {
            if(!hm.containsKey(str[i])){
                answer[i] = -1;
                hm.put(str[i], i);
            }
            else{
                answer[i] = i - hm.get(str[i]);
                hm.put(str[i], i);
            }
        }
        
        return answer;
    }
}