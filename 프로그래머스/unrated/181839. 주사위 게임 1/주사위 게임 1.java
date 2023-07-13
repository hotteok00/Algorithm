class Solution {
    public int solution(int a, int b) {
        return (a%2==0 && b%2==0) ? Math.abs(a-b) : ((a%2!=0&&b%2!=0) ? a*a + b*b : 2 * (a+b));
    }
}