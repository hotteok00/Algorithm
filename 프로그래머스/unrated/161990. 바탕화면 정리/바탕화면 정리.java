class Solution {
    public int[] solution(String[] wallpaper) {
        int lenY = wallpaper[0].length();
        int lenX = wallpaper.length;
        int minX = 50, minY = 50, maxX = 0, maxY = 0;
        
        for(int i = 0; i < lenX; i++) {
            for(int j = 0; j < lenY; j++) {
                if (wallpaper[i].charAt(j) == '#') {
                    if(minX > i) minX = i;
                    if(minY > j) minY = j;
                    if(maxX < i) maxX = i;
                    if(maxY < j) maxY = j;
                }
            }
        }
        maxX++; maxY++;
        
        int[] answer = {minX, minY, maxX, maxY};
        return answer;
    }
}