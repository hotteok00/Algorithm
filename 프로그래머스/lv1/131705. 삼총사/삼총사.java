class Solution {
    int answer = 0;
    
    public int solution(int[] arr) {
        int r = 3;
        int[] comb = new int[r];
        int index = 0;
        int depth = 0;
        
        combination(arr, comb, r, index, depth);
        
        return answer;
    }
    
    void combination(int[] arr, int[] comb, int r, int index, int depth) {
        if(r == 0) {
            int sum = 0;
            for(int i : comb) sum += i;
            if(sum == 0) answer++;
        }
        else if(depth == arr.length) {
            return;
        }
        else{
            comb[index] = arr[depth];
            combination(arr, comb, r - 1, index + 1, depth + 1);
            combination(arr, comb, r, index, depth + 1);
        }
    }
}