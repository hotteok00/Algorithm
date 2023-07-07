import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;

class Solution {
    public int solution(String numbers) {
        int answer = 0;
        
        Set<String> setOfPrimes = new HashSet<>();
        
        List<String> subsetStrings = generateSubsetStrings(numbers.toCharArray());
        for (String subsetString : subsetStrings) {
            List<String> permutations = generatePermutations(subsetString.toCharArray());
            for (String str : permutations)
                if(isPrime(str) && !setOfPrimes.contains(str)) {
                    answer++;
                    setOfPrimes.add(str);
                    // System.out.println("str : " + str);
                }
        }
        
        return answer;
    }
    
     public static List<String> generateSubsetStrings(char[] arr) {
        List<String> subsetStrings = new ArrayList<>();
        generateSubsets(arr, 0, new StringBuilder(), subsetStrings);
        return subsetStrings;
    }

    private static void generateSubsets(char[] arr, int index, StringBuilder current, List<String> subsetStrings) {
        subsetStrings.add(current.toString());

        for (int i = index; i < arr.length; i++) {
            current.append(arr[i]);
            generateSubsets(arr, i + 1, current, subsetStrings);
            current.deleteCharAt(current.length() - 1);
        }
    }
    
    public static List<String> generatePermutations(char[] arr) {
        List<String> permutations = new ArrayList<>();
        generatePermutationsHelper(arr, 0, permutations);
        return permutations;
    }

    private static void generatePermutationsHelper(char[] arr, int index, List<String> permutations) {
        if (index == arr.length - 1) {
            permutations.add(new String(arr));
            return;
        }

        for (int i = index; i < arr.length; i++) {
            swap(arr, index, i);
            generatePermutationsHelper(arr, index + 1, permutations);
            swap(arr, index, i); // backtrack
        }
    }

    private static void swap(char[] arr, int i, int j) {
        char temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    public static boolean isPrime(String str) {
        if (str.charAt(0) == '0') return false;
        
        int number = Integer.parseInt(str);

        if (number <= 1) return false;

        for (int i = 2; i <= Math.sqrt(number); i++)
            if (number % i == 0) return false;

        return true;
    }
}