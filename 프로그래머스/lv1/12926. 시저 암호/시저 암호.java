class Solution {
    public String solution(String s, int n) {
        String answer = "";
        for(int i=0;i<s.length(); i++) {
            if(s.charAt(i) == ' ') {
                answer += " ";
            }
            else{
                if(n + s.charAt(i) > 127) n %= 26;
                char c = (char)(n + s.charAt(i));
                
                // lowercase
                if(s.charAt(i) <= 90) {
                    if(c>=65&&c<=90)
                        answer += c + "";
                    else
                        answer += (char)(c - 26) + "";
                }
                // uppercase
                else {
                    if(c>=97&&c<=122)
                        answer += c + "";
                    else
                        answer += (char)(c - 26) + "";
                }
            }
        }
        return answer;
    }
}