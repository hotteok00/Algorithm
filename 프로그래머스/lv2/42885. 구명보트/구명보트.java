import java.util.Arrays;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        
        Arrays.sort(people);
        
        int idx = 0;
        for(int i = people.length - 1; i >= idx; i--) {
            if(limit >= people[i] + people[idx]) {
                answer++;
                idx++;
            }
            else {
                answer++;
            }
            
            // if(people[i] == 0) continue;
            
            // answer++;
            // int boat = 0;
            // int boatCnt = 0;
            
//             for(int j = i; j >= 0; j--) {
//                 if(people[j] == 0) continue;
                    
//                 if(limit >= boat + people[j]) {
//                     if(boatCnt < 2) {
//                         boat += people[j];
//                         people[j] = 0;
//                         boatCnt++;
//                     }
//                     else break;
//                 }
//             }
            
            
        }
        
        return answer;
    }
}