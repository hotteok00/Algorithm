import java.util.*;

class Solution {
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        
        // 유저 신고 횟수 해시맵
        HashMap<String, Integer> reportCountMap = new HashMap<>();
        for(int i=0; i<id_list.length; i++)
            reportCountMap.put(id_list[i], 0);
        
        // 유저 신고 목록 해시맵
        HashMap<String, Set<String>> reportListMap = new HashMap<>();
        String[] str;
        String reporter;
        String respondent;
        for(int i=0; i<report.length; i++) {
            str = report[i].split(" ");
            reporter = str[0];
            respondent = str[1];
            // System.out.println("reporter : " + reporter);
            // System.out.println("respondent : " + respondent);
            
            if(!reportListMap.containsKey(reporter)) {
                Set<String> v = new HashSet<>();
                v.add(respondent);
                reportListMap.put(reporter, v);
                reportCountMap.put(respondent, 1 + reportCountMap.get(respondent));
            }
            else {
                Set<String> v = reportListMap.get(reporter);
                if(!v.contains(respondent)) { // 기 동일 reporter, 동일 respondent check
                    v.add(respondent);
                    reportListMap.put(reporter, v);
                    reportCountMap.put(respondent, 1 + reportCountMap.get(respondent));
                }
            }
        }
        
        // for(Map.Entry<String, Integer> map : reportCountMap.entrySet())
        //     System.out.println(map.getKey() + " : " + map.getValue());
        
        // 정지된 유저
        ArrayList<String> suspendedUser = new ArrayList<>();
        for(Map.Entry<String, Integer> map : reportCountMap.entrySet()) 
            if(map.getValue() >= k) suspendedUser.add(map.getKey());
    
        for(int i=0; i<id_list.length; i++) {
            if(reportListMap.containsKey(id_list[i])) {
                Set<String> v = reportListMap.get(id_list[i]);
                for(String name : v)
                    if(suspendedUser.contains(name)) answer[i]++;
            }
        }
        
        return answer;
    }
}