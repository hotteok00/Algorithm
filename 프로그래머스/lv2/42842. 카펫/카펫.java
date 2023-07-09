class Solution {
    public int[] solution(int brown, int yellow) {
        int[] answer = new int[2];
        
        int area = brown + yellow;
        
        int x, y;
        for(int i=3; i<area; i++) {
            if(area % i == 0) {
                x = i;
                y = area/i;
                
                if(x < y) continue;
                if(2 * x + 2 * (y - 2) == brown) {
                    answer[0] = x;
                    answer[1] = y;
                    break;
                }
            }
        }
        
        return answer;
    }
}