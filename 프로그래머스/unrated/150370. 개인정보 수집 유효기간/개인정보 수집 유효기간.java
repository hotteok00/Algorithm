import java.util.HashMap;
import java.util.ArrayList;
class Solution {
    public int[] solution(String today, String[] terms, String[] privacies) {
        int[] answer = {};
        
        HashMap<String, Integer> termsMap = new HashMap<>();
        for(String s : terms) {
            String[] tmp = s.split(" ");
            termsMap.put(tmp[0], Integer.parseInt(tmp[1]));
        }
        
        Date criteria = new Date(today);
        ArrayList<Integer> al = new ArrayList<>();
        for(int i=0; i<privacies.length; i++) {
            String[] tmp = privacies[i].split(" ");
            
            Date target = new Date(tmp[0]);
            target.setDate(termsMap.get(tmp[1]));
            
            if(target.compareTo(criteria) == -1) al.add(i + 1);
       }
        
        answer = new int[al.size()];
        int idx = 0;
        for(int i : al) answer[idx++] = i;
        return answer;
    }
    
    class Date implements Comparable<Date> {
        int yyyy;
        int MM;
        int DD;
    
        Date(String today) {
            String[] dates = today.split("\\.");
            this.yyyy = Integer.parseInt(dates[0]);
            this.MM = Integer.parseInt(dates[1]);
            this.DD = Integer.parseInt(dates[2]);
        }
        
        void setDate(int M) {
            if (M >= 12) {
                this.yyyy += M/12; 
                M %= 12;
            }
            
            if(this.MM + M > 12) {
                this.yyyy++;
                this.MM = (this.MM + M) % 12;
            }
            else this.MM += M;
            
            if(this.DD - 1 == 0) {
                if(this.MM - 1 == 0) {
                    this.yyyy--; 
                    this.MM = 12;
                }
                else this.MM--;
                this.DD = 28;
            }
            else this.DD--;
            
            // System.out.println(this);
        }
        
        public String toString() {
            return this.yyyy + "." + this.MM + "." + this.DD;
        }
        
        public int compareTo(Date d) {
            if(this.yyyy > d.yyyy) return 1;
            else if(this.yyyy == d.yyyy) {
                if(this.MM > d.MM) return 1;
                else if(this.MM == d.MM) {
                    if(this.DD > d.DD) return 1;
                    else if(this.DD == d.DD) return 0;
                    else return -1;
                }
                else return -1;
            }
            else return -1;
        }
    }
}