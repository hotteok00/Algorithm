import java.util.Arrays;
import java.util.Set;
import java.util.HashSet;

class Solution {
    public boolean solution(String[] phone_book) {
        Set<String> phone_set = new HashSet<>();
        
        Arrays.sort(phone_book, (String s1, String s2) -> {
            if (s1.length() != s2.length()) {
                return s1.length() - s2.length();
            } else {
                return s1.compareTo(s2);
            }
        });
        // for(String std: phone_book) System.out.println(std);
        
        for(int i=0; i<phone_book.length; i++) {
            String std = phone_book[i];
                
            String tmp = null;
            for(int j=1; j<std.length()+1; j++) {
                // if (check_prefix(std, phone_book[j])) return false;
                tmp = std.substring(0, j);
                if (phone_set.contains(tmp)) return false;
            }
            if (tmp != null) phone_set.add(tmp);
            
            // System.out.println(tmp);
        } 
        
        return true;
    }
    
    private boolean check_prefix(String std, String trg) {
        int len_std = std.length();        
        String trg_prefix = trg.substring(0, len_std);     
        if (std.equals(trg_prefix)) return true;
        return false;
    }
}