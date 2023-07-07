class Solution {
    public int solution(int a, int b, int n) {
        int answer = 0;
        
        while(n >= a) {
            int tmp = 0;
            tmp += (n / a) * b;
            answer += tmp;
            tmp += n % a;
            n = tmp;
            System.out.println(answer);
        }
        
        return answer;
    }
}