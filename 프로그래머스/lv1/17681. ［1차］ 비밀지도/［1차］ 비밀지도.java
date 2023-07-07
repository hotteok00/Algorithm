class Solution {
    public String[] solution(int n, int[] arr1, int[] arr2) {
        String[] answer = new String[n];
        
        String[] map1 = intToBinary(n, arr1);
        System.out.println();
        String[] map2 = intToBinary(n, arr2);
        
        for(int i = 0; i<n; i++) {
            String ans = "";
            String s1 = map1[i];
            String s2 = map2[i];
            
            for(int j = 0; j < n; j++) {
                if(s1.charAt(j) == '0' && s2.charAt(j) == '0') ans += " ";
                else ans += "#";
            }
            answer[i] = ans;
        }
        
        
        return answer;
    }
    
    String[] intToBinary(int n, int[] arr) { 
        String[] map = new String[n];
        
        for(int i = 0; i < n; i++) {
            String result = Integer.toBinaryString(arr[i]);
            String resultWithPadding = String.format("%" + n + "s", result).replaceAll(" ", "0");
            map[i] = resultWithPadding;
        }
        
        for(String s : map)System.out.print(s + " ");
        return map;
    }
}