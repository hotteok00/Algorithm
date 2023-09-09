import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int[] arr = new int[31];
        int[] m = new int[2];
        
        for(int i=0; i<28; i++) arr[sc.nextInt()] = 1;
        
        int flag = 0;
        for(int i=1; i<31; i++) if (arr[i] == 0) m[flag++] = i;
        
        for(int i=0; i<2; i++) System.out.println(m[i]);
        
        sc.close();
    }
}