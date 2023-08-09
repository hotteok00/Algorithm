class Solution {
    public int solution(int[] num_list) {
        if(checkSum(num_list) <= 0) return 1;
        else return 0;
    }
    
    int checkSum(int[] num_list) {
        int a = 1;
        int b = 0;
        
        for(int i : num_list) a *= i;
        for(int i : num_list) b += i;
        b *= b;
        
        return a - b;
    }
}