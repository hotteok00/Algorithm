// import java.util.Arrays;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

class Solution {
//     private int numLength;
    
//     public String solution(int[] numbers) {
//         setNumLength(numbers);
//         ArrayList<String> al = getStringPermutation(numbers);
//         Collections.sort(al);
//         return al.get(al.size() - 1);
//     }
    
//     void setNumLength(int[] numbers) {
//         StringBuilder str = new StringBuilder();
//         for(int i : numbers) str.append(i);
//         numLength = str.toString().length();
//     }
    
//     ArrayList<String> getStringPermutation(int[] numbers) {
//         ArrayList<String> al = new ArrayList<>();
//         makePermutation(numbers, al, 0);
//         return al;
//     }
    
//     void makePermutation(int[] numbers, ArrayList<String> al, int idx) {
//         if(idx == numbers.length - 1) {
//             al.add(cvtStrToInt(numbers));
//             return;
//         }
        
//         for(int i = idx; i < numbers.length; i++) {
//             swap(numbers, idx, i);
//             makePermutation(numbers, al, idx + 1);
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
                StringBuilder sb1 = new StringBuilder(); 
                String str1 = sb1.append(i1).append(i2).toString();
                
                StringBuilder sb2 = new StringBuilder(); 
                String str2 = sb2.append(i2).append(i1).toString();
                
                return Integer.parseInt(str2) - Integer.parseInt(str1);
            }
        });
        
        StringBuilder sb = new StringBuilder();
        for(Integer i : al) sb.append(i);
        return (sb.toString().charAt(0) == '0') ? "0" : sb.toString();
    }
}