import java.util.*;

class Solution {
    public int solution(int[][] board, int[] moves) {
        int answer = 0;
        
        int n = board.length;
        int[][] tmp = new int[n][n];
        for(int i=0; i<n; i++) {
            for(int j=0; j<n; j++) {
                tmp[i][j] = board[j][i];
                System.out.print(tmp[i][j] + " ");
            }
            System.out.println();
        }
        board = tmp;
        
        ArrayList<Stack<Integer>> als = new ArrayList<>();
        // for(int[] i : board) {
        //     Stack<Integer> stack = new Stack<>();
        //     for(int j : i)  if (j != 0) {stack.push(j);System.out.print(j + " ");}
        //     System.out.println();
        //     als.add(stack);
        // }
        for(int i=0; i<n; i++) {
            Stack<Integer> stack = new Stack<>();
            for(int j=n-1; j>=0; j--) 
                if(tmp[i][j] != 0) {stack.push(tmp[i][j]); System.out.print(tmp[i][j] + " ");}
            System.out.println();
            als.add(stack);
        }
        
        Stack<Integer> goal = new Stack<>();
        for(int i : moves) {
            Stack<Integer> stack = als.get(i-1);
            if(stack.empty()) continue;
            else {
                int mv = stack.pop();
                System.out.print(mv);
                if(goal.empty()) goal.push(mv);
                else {
                    if (goal.peek() == mv) {
                        goal.pop(); 
                        answer+=2;
                    }
                    else goal.push(mv);
                }
            }
            als.set(i-1, stack);
        }
        
        return answer;
    }
}