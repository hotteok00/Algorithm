import java.util.PriorityQueue;
class Solution {
    public int[] solution(int k, int[] score) {
        int[] answer = new int[score.length];
        int idx = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for(int i : score) {
            if(pq.size() < k) {
                pq.add(i);
                answer[idx++] = pq.peek();
            }
            else{
                if(pq.peek() < i){
                    pq.poll();
                    pq.add(i);
                    answer[idx++] = pq.peek();
                }
                else 
                    answer[idx++] = pq.peek();
            }
        }
        
        return answer;
    }
}