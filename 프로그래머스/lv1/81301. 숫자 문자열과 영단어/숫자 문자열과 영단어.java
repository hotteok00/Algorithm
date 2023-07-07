import java.util.HashMap;

class Solution {
    public int solution(String s) {
        String answer = "";
        HashMap<String, String> hm = new HashMap<>();
        hm.put("zero","0");
        hm.put("one","1");
        hm.put("two","2");
        hm.put("three","3");
        hm.put("four","4");
        hm.put("five","5");
        hm.put("six","6");
        hm.put("seven","7");
        hm.put("eight","8");
        hm.put("nine","9");
        
        String tmp = "";
        for(int i=0; i<s.length(); i++) {
            tmp += s.substring(i, i+1);
            if(hm.containsKey(tmp)) {
                answer += hm.get(tmp);
                tmp = "";
            }
            else if(isNumeric(tmp)) {
                answer += tmp;
                tmp = "";
            }
        }
        
        return Integer.parseInt(answer);
    }
    
    public static boolean isNumeric(String s) {
        try {
            Double.parseDouble(s);
            return true;
        } catch (NumberFormatException e) {
            return false;
        }
    }
}