import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;

class Solution {
    public int[] solution(int N, int[] stages) {
        int[] answer = new int[N];
        
        int players = stages.length;
        int[] numberOfPlayersOnStage = new int[N+2];
        int[] numberOfPlayersCleared = new int[N+2];
        for(int i : stages) numberOfPlayersOnStage[i]++;
        for(int i = 1; i < N+2; i++) 
            for(int j = i; j < N+2; j++)
                numberOfPlayersCleared[i] += numberOfPlayersOnStage[j];
        
        double[] failureRate = new double[N+2];
        for(int i = 1; i < N+2; i++){
            if(numberOfPlayersCleared[i] == 0) {
                failureRate[i] = 0;
                continue;
            }
            failureRate[i] = (double)numberOfPlayersOnStage[i] / numberOfPlayersCleared[i];
        }
        
        ArrayList<stageFailureRate> al = new ArrayList<>();
        for(int i = 1; i < N+1; i++) 
            al.add(new stageFailureRate(i, failureRate[i]));
        
        Collections.sort(al, new Comparator<stageFailureRate>(){ 		
			public int compare(stageFailureRate sf1, stageFailureRate sf2) { 			
				if(sf1.failureRate == sf2.failureRate)			
					return Integer.compare(sf1.stage, sf2.stage);
				return Double.compare(sf2.failureRate, sf1.failureRate);
			}
		});
        
        int idx = 0;
        for(stageFailureRate sf : al) answer[idx++] = sf.stage;
        return answer;
    }
    
    class stageFailureRate {
        int stage;
        double failureRate;
        stageFailureRate(int stage, double failureRate) {
            this.stage = stage;
            this.failureRate = failureRate;
        }
    }
}