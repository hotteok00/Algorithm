import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> record = new HashMap<>();
        int length;
        
        length = completion.length;
        for(int i=0; i<length; i++) {
            String tmp = completion[i];
            if(!record.containsKey(tmp))
                record.put(tmp, 1);
            else
                record.put(tmp, record.get(tmp) + 1);
        }

        length = participant.length;
        for(int i=0; i<length; i++) {
            String tmp = participant[i];
            if(record.containsKey(tmp)) 
                record.put(tmp, record.get(tmp) - 1);
            else 
                return tmp;
            
            if(record.get(tmp) == 0) record.remove(tmp);
        }
        
        return answer;
    }
}