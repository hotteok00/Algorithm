class Solution {
    public int solution(String t, String p) {
        int answer = 0;

        int f = p.length();
        for(int i=0; i<=t.length()-f; i++)
            if(p.compareTo(t.substring(i, i+f)) >= 0) 
                answer++;
        
        return answer;
    }
}