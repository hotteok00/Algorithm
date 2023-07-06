import java.util.HashMap;
class Solution {
    public String solution(String[] survey, int[] choices) {
        String answer = "";
        
        // survey[i]의 첫 번째 캐릭터는 i+1번 질문의 "비동의" 관련 선택지
        // survey[i]의 두 번째 캐릭터는 i+1번 질문의 "동의" 관련 선택지
        
        HashMap<String, Integer> kbti = new HashMap<>();
        kbti.put("RT", 0); kbti.put("CF", 0); kbti.put("JM", 0); kbti.put("AN", 0);
        
        int score;
        for(int i=0; i<choices.length; i++) {
            score = choices[i] - 4;
            if (kbti.containsKey(survey[i]))
                kbti.put(survey[i], kbti.get(survey[i]) + score);
            else {
                score *= -1;
                String tmp = survey[i]; 
                survey[i] = "" + tmp.charAt(1) + tmp.charAt(0);
                kbti.put(survey[i], kbti.get(survey[i]) + score);
            }
        }
        
        
        if (kbti.get("RT") != 0) {
            if(kbti.get("RT") > 0) answer += "T";
            else answer += "R";
        }
        else answer += "R";
        if (kbti.get("CF") != 0) {
            if(kbti.get("CF") > 0) answer += "F";
            else answer += "C";
        }
        else answer += "C";
        if (kbti.get("JM") != 0) {
            if(kbti.get("JM") > 0) answer += "M";
            else answer += "J";
        }
        else answer += "J";
        if (kbti.get("AN") != 0) {
            if(kbti.get("AN") > 0) answer += "N";
            else answer += "A";
        }
        else answer += "A";
        
        return answer;
    }
}