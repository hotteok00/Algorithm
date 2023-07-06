class Solution {
    public int[] solution(String[] park, String[] routes) {
        int[] answer = new int[2];
        int I = 0, J = 0;
        
        String[][] p = new String[park.length][park[0].length()];
        for(int i=0; i<park.length; i++) p[i] = park[i].split("");
        
        String[][] r = new String[routes.length][2];
        for(int i=0; i<routes.length; i++) r[i] = routes[i].split(" ");
        
        // find s
        for(int i=0; i<p.length; i++) {
            for(int j=0; j<p[0].length; j++) {
                if(p[i][j].equals("S")) {
                    I = i;
                    J = j;
                    i = p.length;
                    break;
                }
            }
        }
        
        boolean flag;
        for(int i=0; i<r.length; i++) {
            flag = false;
            
            int d = Integer.parseInt(r[i][1]);
            switch(r[i][0]) {
                case "N":
                    for(int j=1; j<=d; j++) {
                        if(I - j < 0) {flag = true; break;}
                        if(p[I - j][J].equals("X")) {flag = true; break;}
                    }
                    if(flag) continue;
                    I -= d;
                    break;
                case "S":
                    for(int j=1; j<=d; j++) {
                        if(I + j >= p.length) {flag = true; break;}
                        if(p[I + j][J].equals("X")) {flag = true; break;}
                    }
                    if(flag) continue;
                    I += d;
                    break;
                case "W":
                    for(int j=1; j<=d; j++) {
                        if(J - j < 0) {flag = true; break;}
                        if(p[I][J - j].equals("X")) {flag = true; break;}
                    }
                    if(flag) continue;
                    J -= d;
                    break;
                case "E":
                    for(int j=1; j<=d; j++) {
                        if(J + j >= p[0].length) {flag = true; break;}
                        if(p[I][J + j].equals("X")) {flag = true; break;}
                    }
                    if(flag) continue;
                    J += d;
                    break;
            }
        }
        
        answer[0] = I;
        answer[1] = J;
        return answer;
    }
}