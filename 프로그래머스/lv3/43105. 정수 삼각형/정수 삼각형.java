import java.util.Arrays;
class Solution {
    public int solution(int[][] triangle) {
        int Clength = triangle.length;
        for(int i = 1; i < Clength; i++) {
            int Rlength = triangle[i].length;
            for(int j = 0; j < Rlength; j++) {
                if(j == 0) {
                    triangle[i][j] += triangle[i - 1][j];
                    continue;
                }
                
                if(j == triangle[i].length - 1) {
                    triangle[i][j] += triangle[i - 1][j - 1];
                    continue;
                }
                
                triangle[i][j] += Math.max(triangle[i - 1][j - 1], triangle[i - 1][j]);
            }
        }
        
        return Arrays.stream(triangle[Clength - 1]).max().getAsInt();
    }
}