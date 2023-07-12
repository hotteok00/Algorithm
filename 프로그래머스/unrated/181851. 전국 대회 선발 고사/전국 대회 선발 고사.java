import java.util.*;
class Solution {
    public int solution(int[] rank, boolean[] attendance) {
        ArrayList<node> al = new ArrayList<>();
        for(int i=0; i<rank.length; i++) if(attendance[i]) al.add(new node(i, rank[i]));
        
        Collections.sort(al, new Comparator<node>() {
            public int compare(node n1, node n2) {
                return n1.rank - n2.rank;
            }
        });
        
        return 10000 * al.get(0).idx + 100 * al.get(1).idx + al.get(2).idx;
    }
    
    class node {
        int idx;
        int rank;
        
        node(int i, int r) {
            this.idx = i;
            this.rank = r;
        }
    }
}