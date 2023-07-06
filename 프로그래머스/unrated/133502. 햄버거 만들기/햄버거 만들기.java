import java.util.Stack;

class Solution {
    public int solution(int[] ingredient) {
        int answer = 0;
        
//         String str, prev;
//         StringBuilder sb = new StringBuilder();
//         for(int i : ingredient) sb.append(i);
//         str = sb.toString();
        
//         while(true) {
//             prev = str;
//             str = str.replaceFirst("1231", "");
//             if (str.equals(prev)) break;
//         }
        
//         answer = (ingredient.length - str.length()) / 4;
        
        
        int[] pack = {1, 2, 3, 1};
        boolean flag;
        for(int i=0, length = ingredient.length; i<length; i++) {
            if (ingredient[i] == 1 && i + 4 <= length) {
                flag = true;
                for(int j = i + 1; j < i + 4; j++) {
                    if (pack[j - i] != ingredient[j]) {
                        flag = false;
                        i = j - 1;
                        break;
                    }
                }
                if (flag) {
                    for(int j = i; j < length - 4; j++) ingredient[j] = ingredient[j + 4];
                    
                    if (i > 4) i -= 4;
                    else i = -1;
                    
                    length -= 4;
                    answer++;
                }
            }
        }

        return answer;
    }
}