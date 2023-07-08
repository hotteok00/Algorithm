import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

class Main{
    static int zero;
    static int one;
    static class Fibo{
        int zero;
        int one;
        int fibo;
        Fibo(int z, int o, int f) {
            this.zero = z;
            this.one = o;
            this.fibo = f;
        }
    }
    static Fibo[] fibo;
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        initNum();
        fibo = new Fibo[41];
        
        int n = Integer.parseInt(br.readLine());
        for(int i=0; i<n; i++) {
            int tmp = Integer.parseInt(br.readLine());
            fibonacci(tmp);
            sb.append(fibo[tmp].zero).append(' ').append(fibo[tmp].one).append('\n');
        }
        
        System.out.println(sb.toString());
    }
    
    static void initNum() {
        zero = 0;
        one = 0;
    }
    
    static void fibonacci(int n) {
        for(int i=0; i<=n; i++) {
            if(i == 0) {
                if(fibo[i] == null) fibo[i] = new Fibo(1, 0, 0);
                continue;
            }
            if(i == 1) {
                if(fibo[i] == null) fibo[i] = new Fibo(0, 1, 1);
                continue;
            }
            
            if(fibo[i] == null) 
                fibo[i] = new Fibo(fibo[i-1].zero + fibo[i-2].zero, 
                                   fibo[i-1].one + fibo[i-2].one, 
                                   fibo[i-1].fibo + fibo[i-2].fibo);
        }
    }
}