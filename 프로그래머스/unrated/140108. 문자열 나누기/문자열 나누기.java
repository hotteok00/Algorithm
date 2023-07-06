class Solution {
    public int solution(String s) {
        int answer = 0;
        
        char firstX;
        int x, y, i, l;
        while(s.length() > 0) {
            firstX = s.charAt(0);
            x = 1; y = 0;
            l = s.length();
            for(i=1; i<l; i++) {
                if(s.charAt(i) == firstX) x++;
                else y++;
                
                if (x == y) {
                    s = s.substring(i + 1, l);
                    break;
                }
            }
            
            if (i == l) {
                answer++;
                break;
            }
            answer++;
        }
        
        return answer;
    }
}