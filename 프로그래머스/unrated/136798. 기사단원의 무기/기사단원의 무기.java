class Solution {
    public int solution(int number, int limit, int power) {
        int answer = 0;
        
        int[] templars = new int[number + 1];
        for(int i = 1; i <= number; i++) {
            templars[i] = getNumberOfDivisor(i);
            if(templars[i] > limit) templars[i] = power;
            answer += templars[i];
        }
        
        return answer;
    }
    
    int getNumberOfDivisor(int n) {
        int cnt = 0;
        for(int i = 1; i * i <= n; i++) {
            if (i * i == n) cnt++;
            else if (n % i == 0) cnt += 2;
        }
        return cnt;
    }
}