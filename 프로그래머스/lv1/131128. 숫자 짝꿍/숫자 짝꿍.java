import java.util.Collections;
import java.util.Comparator;
import java.util.ArrayList;
import java.util.HashMap;

class Solution {
    public String solution(String X, String Y) {
        String answer = "";
        int length;
        
        
        String[] y = Y.split("");
        HashMap<String, Integer> hm_y = new HashMap<>();
        for(String s : y) hm_y.put(s, hm_y.getOrDefault(s, 0) + 1);
        // length = Y.length();
        // HashMap<Character, Integer> hm_y = new HashMap<>();
        // for(int i=0; i<length; i++) {
        //     Character c = Y.charAt(i);
        //     hm_y.put(c, hm_y.getOrDefault(c, 0) + 1);
        // }
        
        String[] x = X.split("");
        ArrayList<String> al = new ArrayList<>();
        for(String s : x) 
            if (hm_y.containsKey(s) && hm_y.get(s) > 0) {
                al.add(s);
                hm_y.put(s, hm_y.get(s) - 1);
            }
        // length = X.length();
        // ArrayList<Character> al = new ArrayList<>();
        // for(int i=0; i<length; i++) {
        //     Character c = X.charAt(i);
        //     if (hm_y.containsKey(c) && hm_y.get(c) > 0) {
        //         al.add(c);
        //         hm_y.put(c, hm_y.get(c) - 1);
        //     }
        // }
        
        StringBuilder sb = new StringBuilder();
        Collections.sort(al, Comparator.reverseOrder());
        for(String s : al) sb.append(s);
        // for(Character c : al) sb.append(c);
        answer = sb.toString();
        
        if (answer.equals("")) return "-1";
        else {
            if (answer.charAt(0) == '0') return "0";
            return answer;
        }
    }
}