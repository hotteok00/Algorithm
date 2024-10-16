import java.util.*;

class Solution {
    class Data {
        int idx;
        int value;
        
        Data(int idx, int value) {
            this.idx = idx;
            this.value = value;
        }
        
        @Override
        public String toString() {
            return "idx:"+idx+" value:"+value;
        }
    }
    
    public int[] solution(int[] prices) {
        int len = prices.length;
        
        int[] ans = new int[len];
        
        Stack<Data> stack = new Stack<>();
        for (int i=0; i<len; i++) {
            int price = prices[i];
            
            while (stack.size() > 0 && stack.peek().value > price) {
                Data data = stack.pop();
                ans[data.idx] = i - data.idx;
            }
            
            stack.push(new Data(i, price));
        }
        
        while(stack.size() > 0) {
            Data data = stack.pop();
            ans[data.idx] = len - data.idx - 1;
        }
        
        return ans;
    }
}