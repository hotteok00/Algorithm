import java.util.*;

class Solution {
    public String[] solution(String[] strings, int n) {
        Arrays.sort(strings, new Comparator<String>() {
	        public int compare(String s1, String s2) {
                String a = s1.substring(n, n+1);
                String b = s2.substring(n, n+1);
                
                if(a.equals(b)) 
                    return s1.compareTo(s2);
                else
		            return a.compareTo(b);
	        }
        });
        
        return strings;
    }
}