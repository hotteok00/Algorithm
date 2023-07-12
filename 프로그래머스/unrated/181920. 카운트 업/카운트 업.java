class Solution {
    public int[] solution(int start, int end) {
        int l = end - start;
        int[] answer = new int[l + 1];
        for(int i = 0; i <= l; i++) answer[i] = start + i;
        return answer;
    }
}