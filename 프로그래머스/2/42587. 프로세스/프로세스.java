import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(int[] priorities, int location) {
        int answer = 1;
        
        Queue<Integer> queue = new LinkedList<Integer>();
        int[] priorities_check = new int[10];   // 배열 우선 순위 check
        for (int i = 0; i < priorities.length; i++) {
            queue.add(priorities[i]);
            priorities_check[priorities[i]]++;
        }
        
        int size = priorities.length;
        for (int i = 9; i > 0; i--) {
            for (int j = priorities_check[i]; j > 0; j--) {
                while(true) {
                    Integer crt = queue.poll();
                    
                    if (crt == i) {
                        if (location == 0) return answer;
                        
                        location = next_location(location, size);
                        size--;
                        answer++;
                        break;
                    }
                    location = next_location(location, size);
                    
                    queue.add(crt);
                }
                // System.out.println(queue + ":" + location);
            }
        }
        
        return answer;
    }
    
    private int next_location(int location, int size) {
        if (location == 0) return size-1;
        else return location-1;
    }
}