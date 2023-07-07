class Solution {
    public int[] solution(int[] answers) {
        int[] answer = new int[0];
        
        int u1 = 0; int[] arr1 = {1,2,3,4,5};
        int u2 = 0; int[] arr2 = {2,1,2,3,2,4,2,5};
        int u3 = 0; int[] arr3 = {3,3,1,1,2,2,4,4,5,5};
        
        for(int i=0; i<answers.length; i++) {
            if(arr1[i%arr1.length] == answers[i]) u1++;
            if(arr2[i%arr2.length] == answers[i]) u2++;
            if(arr3[i%arr3.length] == answers[i]) u3++;
        }
        
             if(u1 > u2 && u1 > u3) {answer = new int[1]; answer[0] = 1;}
        else if(u2 > u1 && u2 > u3) {answer = new int[1]; answer[0] = 2;}
        else if(u3 > u1 && u3 > u2) {answer = new int[1]; answer[0] = 3;}
        else if(u1 > u3 && u1 == u2) {answer = new int[2]; answer[0] = 1; answer[1] = 2;}
        else if(u1 > u2 && u1 == u3) {answer = new int[2]; answer[0] = 1; answer[1] = 3;}
        else if(u2 > u1 && u2 == u3) {answer = new int[2]; answer[0] = 2; answer[1] = 3;}
        else if(u1 == u2 && u1 == u3) {answer = new int[3]; answer[0] = 1; answer[1] = 2; answer[2] = 3;}
        
        return answer;
    }
}