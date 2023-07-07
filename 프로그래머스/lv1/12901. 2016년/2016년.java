import java.util.HashMap;

class Solution {
    public String solution(int a, int b) {
        String answer = "";
        
        HashMap<Integer, String> c = new HashMap<>();
        c.put(0, "SAT");
        c.put(1, "SUN");
        c.put(2, "MON");
        c.put(3, "TUE");
        c.put(4, "WED");
        c.put(5, "THU");
        c.put(6, "FRI");

        int year = 2016;
        if (a < 3) {
            a += 12;
            year--;
        }
        
        int q = b;
        int m = a;
        int K = year % 100;
        int J = year / 100;
        
        int h = (q + (13 * (m + 1) / 5) + K + (K / 4) + (J / 4) - (2 * J)) % 7;
        if (h < 0) h += 7;
        
        answer = c.get(h);
        
        return answer;
    }
}