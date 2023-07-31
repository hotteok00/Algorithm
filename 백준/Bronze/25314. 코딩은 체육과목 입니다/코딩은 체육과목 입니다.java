import java.util.*;

class Main {
    public static void main (String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int N = sc.nextInt();
        String str = getLong(N);
        
        System.out.println(str + "long int");
        
        sc.close();
    }
    
    static String getLong(int N) {
        StringBuilder sb = new StringBuilder();
        
        for(int i = 1; i < N/4; i++)
            sb.append("long ");
        
        return sb.toString();
    }
}