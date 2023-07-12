class Solution {
    public int[] solution(int[] arr) {
        for(int i=0; i<arr.length; i++) {
            int tmp = arr[i];
                 if(tmp >= 50 && tmp % 2 == 0) arr[i] = tmp / 2;
            else if(tmp < 50 && tmp % 2 != 0) arr[i] = tmp * 2;
        }
        return arr;
    }
}