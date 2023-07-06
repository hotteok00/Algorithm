import java.util.HashMap;

class Solution {
    public String[] solution(String[] players, String[] callings) {        
        String[] answer = players;
        
        HashMap<String, Integer> p_seq = new HashMap<>();
        HashMap<Integer, String> i_seq = new HashMap<>();
        for(int i = 0; i < players.length; i++) {
            p_seq.put(players[i], i);
            i_seq.put(i, players[i]);
        }
        
        for(int i=0; i<callings.length; i++) {
            int j = p_seq.get(callings[i]);
            
            String k_1 = i_seq.get(j);
            String k_2 = i_seq.get(j-1);
            
            p_seq.put(k_1, j-1);
            p_seq.put(k_2, j);
            
            i_seq.put(j-1, k_1);
            i_seq.put(j, k_2);
            
            exch(answer, j, j-1);
        }
        
        return answer;
    }
    
    void exch(String[] list, int i, int j){
        String tmp = list[i];
        list[i] = list[j];
        list[j] = tmp;
    }
}