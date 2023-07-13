import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

class Solution {
//     private int numLength;
    
//     public String solution(int[] numbers) {
//         setNumLength(numbers);
//         ArrayList<String> al = getStringCombination(numbers);
//         Collections.sort(al);
//         return al.get(al.size() - 1);
//     }
    
//     void setNumLength(int[] numbers) {
//         StringBuilder str = new StringBuilder();
//         for(int i : numbers) str.append(i);
//         numLength = str.toString().length();
//     }
    
//     ArrayList<String> getStringCombination(int[] numbers) {
//         ArrayList<String> al = new ArrayList<>();
//         makeCombination(numbers, al, 0);
//         return al;
//     }
    
//     void makeCombination(int[] numbers, ArrayList<String> al, int idx) {
//         if(idx == numbers.length - 1) {
//             al.add(cvtStrToInt(numbers));
//             return;
//         }
        
//         for(int i = idx; i < numbers.length; i++) {
//             swap(numbers, idx, i);
//             makeCombination(numbers, al, idx + 1);
//             swap(numbers, idx, i);
//         }
//     }
    
//     void swap(int[] numbers, int i, int j) {
//         int temp = numbers[i];
//         numbers[i] = numbers[j];
//         numbers[j] = temp;
//     }
    
//     String cvtStrToInt(int[] numbers) {
//         StringBuilder str = new StringBuilder();
//         for(int i : numbers) str.append(i);
//         return str.toString();
//     }
    
    public String solution(int[] numbers) {
        ArrayList<Integer> al = new ArrayList<>();
        for(int i : numbers) al.add(i);
        
        Collections.sort(al, new Comparator<Integer>() {
            public int compare(Integer i1, Integer i2) {
//                 if(i1 == i2) return 0;
                
//                 int cnt1 = getCnt(i1);
//                 int cnt2 = getCnt(i2);
                
//                 while(cnt1 > 0 && cnt2 > 0) {
//                     int tmp1 = i1 / cnt1;
//                     int tmp2 = i2 / cnt2;
//                     if(tmp1 == tmp2) {                        
//                         if(cnt1 < 10 && cnt2 < 10) break;
//                         if(cnt1 > 9) {i1 -= (tmp1) * cnt1; cnt1 /= 10;}
//                         if(cnt2 > 9) {i2 -= (tmp2) * cnt2; cnt2 /= 10;}
//                     }
//                     else return tmp2 - tmp1;
//                 }
                
//                 return i2 - i1;
                StringBuilder sb1 = new StringBuilder(); 
                sb1.append(i1).append(i2);
                String str1 = sb1.toString();
                
                StringBuilder sb2 = new StringBuilder(); 
                sb2.append(i2).append(i1);
                String str2 = sb2.toString();
                
                return Integer.parseInt(str2) - Integer.parseInt(str1);
            }
            
//             int getCnt(int i) {
//                 int cnt = 1;
//                 while(i > 9) {
//                     i /= 10;
//                     cnt *= 10;
//                 }
//                 return cnt;
//             }
        });
        
        StringBuilder sb = new StringBuilder();
        for(Integer i : al) sb.append(i);
        return (sb.toString().charAt(0) == '0') ? "0" : sb.toString();
    }
}