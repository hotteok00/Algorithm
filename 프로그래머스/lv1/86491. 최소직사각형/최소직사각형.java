class Solution {
    public int solution(int[][] sizes) {
        for(int[] i : sizes) {
            if(i[0] < i[1]){
                int tmp = i[0];
                i[0] = i[1];
                i[1] = tmp;
            }
        }
        
        int max_w = 0;
        int max_h = 0;
        for(int i=1; i<sizes.length; i++) { 
            if(sizes[max_w][0] < sizes[i][0]) { max_w = i; }
            if(sizes[max_h][1] < sizes[i][1]) { max_h = i; }
        }
        
        return sizes[max_w][0] * sizes[max_h][1];
    }
}