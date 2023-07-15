import java.util.ArrayList;
class Solution {
    public int[] solution(int[] arr) {
        ArrayList<Integer> answer = new ArrayList<>();
        for(int i : arr) {
            for(int j = 0; j < i; j++) answer.add(i);
        }
        arr = new int[answer.size()];
        for(int i=0; i<answer.size(); i++) arr[i] = answer.get(i);
        return arr;
    }
}