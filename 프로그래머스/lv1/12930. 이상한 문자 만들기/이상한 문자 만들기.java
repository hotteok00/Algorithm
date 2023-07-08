class Solution {
    public String solution(String s) {
        String[] strArr = s.split(" ");
        String answer = "";
        
        for(int i=0; i<strArr.length; i++){
            for(int j=0; j<strArr[i].length(); j++){
                String c = String.valueOf(strArr[i].charAt(j));
                if(j%2==0) c = c.toUpperCase();
                else c = c.toLowerCase();
                answer += c;
            }
            answer += " ";
        }
        answer = answer.substring(0, answer.length()-1);
        
        for(int i=s.length()-1; i>=0; i--){
            if(s.charAt(i) == ' ') answer += " ";
            else break;
        }
        
        return answer;
    }
}