class Solution {
    public int solution(String dartResult) {
        int answer = 0;
        
        int length = dartResult.length();
        int[] score = new int[length];
        for(int i=0; i<length; i++) {
            char tmp = dartResult.charAt(i);
            int org = (i != 0) ? score[i-1] : 0;
            switch(tmp) {
                case 'T':
                    score[i-1] *= org;
                case 'D':
                    score[i-1] *= org;
                case 'S':
                    score[i-1] *= 1;
                    break;
                case '*':
                    int cnt = 0;
                    for(int j=i-2; j>=0; j--) {
                        if(cnt >= 2) break;
                        if(score[j] != 0 || dartResult.charAt(j) == '0') {
                            cnt++;
                            score[j] *= 2;
                        }
                    }
                    break;
                case '#':
                    score[i-2] *= -1;
                    break;
                case '0':
                    if(org != 0 && score[i-1] == 1) {
                        score[i-1] = 0; 
                        score[i] = 10;
                    }
                    break;
                default :
                    score[i] = Character.getNumericValue(tmp);
                    break;
            }
        }
        
        for(int i : score) {System.out.println(i); answer += i;}
        return answer;
    }
}