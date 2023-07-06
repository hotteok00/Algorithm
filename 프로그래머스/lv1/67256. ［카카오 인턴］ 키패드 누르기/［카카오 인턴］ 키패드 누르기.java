import java.util.HashMap;
class Solution {
    public String solution(int[] numbers, String hand) {
        StringBuilder answer = new StringBuilder();
        
        Coordinates left = new Coordinates(3, 0);   // *
        Coordinates right = new Coordinates(3, 2);  // #
        
        HashMap<Integer, String> hm = new HashMap<>();
        hm.put(1, "L"); hm.put(4, "L"); hm.put(7, "L");
        hm.put(3, "R"); hm.put(6, "R"); hm.put(9, "R");
        
        HashMap<Integer, Coordinates> hc = new HashMap<>();
        hc.put(1, new Coordinates(0, 0)); hc.put(2, new Coordinates(0, 1)); hc.put(3, new Coordinates(0, 2));
        hc.put(4, new Coordinates(1, 0)); hc.put(5, new Coordinates(1, 1)); hc.put(6, new Coordinates(1, 2));
        hc.put(7, new Coordinates(2, 0)); hc.put(8, new Coordinates(2, 1)); hc.put(9, new Coordinates(2, 2));
                                          hc.put(0, new Coordinates(3, 1));
        
        for(int i : numbers) {
            if(hm.containsKey(i)) {
                String s = hm.get(i);
                answer.append(s);
                if (s.equals("L")) left = hc.get(i);
                else               right = hc.get(i);
            }
            else {
                Coordinates tmp = hc.get(i);
                
                int leftDX = Math.abs(left.x - tmp.x);
                int leftDY = Math.abs(left.y - tmp.y);
                int leftD = leftDX + leftDY;
                
                int rightDX = Math.abs(right.x - tmp.x);
                int rightDY = Math.abs(right.y - tmp.y);
                int rightD = rightDX + rightDY;
                
                // System.out.println("leftDX + leftDY = " + leftDX + " + " + leftDY);
                // System.out.println("rightDX + rightDY = " + rightDX + " + " + rightDY);
                
                if (leftD == rightD) {
                    if(hand.equals("left")) {
                        answer.append("L");
                        left = tmp;
                    }
                    else {
                        answer.append("R");
                        right = tmp;
                    }
                }
                else {
                    if (leftD < rightD) {
                        answer.append("L");
                        left = tmp;
                    }
                    else {
                        answer.append("R");
                        right = tmp;
                    }
                }
            }
        }
        
        return answer.toString();
    }
    
    class Coordinates {
        int x;
        int y;
        
        Coordinates(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}