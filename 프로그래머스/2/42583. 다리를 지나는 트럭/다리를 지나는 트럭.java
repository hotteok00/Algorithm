import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        
        int crt_w = 0;
        int max_w = weight;
        
        Queue<Integer> src_bridge = new LinkedList<>();
        Queue<Integer> now_bridge = new LinkedList<>();
        Queue<Integer> dst_bridge = new LinkedList<>();
        
        for (Integer i : truck_weights) src_bridge.add(i);
        for (int i=0; i<bridge_length; i++) now_bridge.add(0);
        
        while(dst_bridge.size() < truck_weights.length) {
            // System.out.println(answer+" dst:"+dst_bridge+"\t\tnow:"+now_bridge+"\t\tsrc:"+src_bridge);
            
            Integer truck_w = now_bridge.poll();
            
            if (truck_w != null){
                if (truck_w != 0) {
                    dst_bridge.add(truck_w);
                    crt_w -= truck_w;
                }
            }
            
            truck_w = src_bridge.peek();
            
            if (truck_w != null) {
                if (crt_w + truck_w <= max_w) {
                    src_bridge.poll();
                    now_bridge.add(truck_w);
                    crt_w += truck_w;
                }
                else {
                    now_bridge.add(0);
                }
            }
            
            answer++;
        }
        // System.out.println(answer+" dst:"+dst_bridge+"\t\tnow:"+now_bridge+"\t\tsrc:"+src_bridge);
        
        return answer;
    }
}