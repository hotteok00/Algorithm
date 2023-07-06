class Solution {
    public String solution(String new_id) {
        StringBuilder answer = new StringBuilder();
        int length;
        char prev = '\0';
        
        new_id = new_id.toLowerCase();
        length = new_id.length();
        for(int i = 0; i < length; i++) {
            char c = new_id.charAt(i);
            
            if (!(c >= '0' && c <= '9') && // isNumeric
                !(c >= 'a' && c <= 'z') && // isAlpha
                c != '-' && c != '_' && c != '.') 
                continue;
            
            if (prev == '.' && c == '.') continue;
            
            answer.append(c);
            prev = c;
        }
        new_id = answer.toString();
        answer.setLength(0);
        
        length = new_id.length();
        for(int i = 0; i < length; i++) {
            char c = new_id.charAt(i);
            
            if (i == 0 || i == length - 1)
                if (c == '.') continue;
            
            answer.append(c);
        }
        new_id = answer.toString();
        answer.setLength(0);
        
        if (new_id.equals("")) new_id = "a";
        
        length = new_id.length();
        if (length > 15) {
            new_id = new_id.substring(0, 15);
            length = new_id.length();
            for(int i = length - 1; i >= 0; i--) {
                if (new_id.charAt(i) == '.') 
                    new_id = new_id.substring(0, i);
                else
                    break;
            }
        }
        
        length = new_id.length();
        if (length < 3) {
            while (length < 3) {
                new_id += new_id.charAt(length - 1);
                length = new_id.length();
            }
        }
        
        return new_id;
    }
}