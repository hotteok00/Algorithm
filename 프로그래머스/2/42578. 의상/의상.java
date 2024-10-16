import java.util.ArrayList;
import java.util.HashMap;

class Solution {
    public int solution(String[][] clothes) {
        int answer = 1;
        
        HashMap<String, ArrayList<String>> closet = new HashMap<>();
        
        for (int i=0; i<clothes.length; i++) {
            if (closet.containsKey(clothes[i][1])) {
                ArrayList<String> v = closet.get(clothes[i][1]);
                v.add(clothes[i][0]);
            }
            else {
                ArrayList<String> new_v = new ArrayList<>();
                new_v.add(clothes[i][0]);
                
                closet.put(clothes[i][1], new_v);
            }
        }
        
        // 옷이 올바르게 분류되었는지 확인
        // System.out.println("옷 분류 결과:");
        for (String category : closet.keySet()) {
            // System.out.println(category + ": " + closet.get(category));
            
            answer *= (closet.get(category).size() + 1);
        }
        
        return answer-1;
    }
}