// import java.util.Scanner;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException {
		// Scanner sc = new Scanner(System.in);
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        
        int length = 1000001;
        int[] arr = new int[length];
            
        for(int i = 2; i < length; i++)
            if(arr[i] == 0) {
                arr[i] = i;
                for(int j = 2 * i; j < length; j+= i) arr[j] = -1;
            }
        
        int n; String str; boolean flag;
        while((str = reader.readLine()) != null) {
            if((n = Integer.parseInt(str)) == 0) break;
            flag = true;
            for(int i = 3; i < n; i += 2) {
                if(arr[i] != -1 && arr[n - i] != -1) {
                    System.out.println(n + " = " + arr[i] + " + " + arr[n - i]);
                    flag = false;
                    break;
                }
            }
            if(flag) System.out.println("Goldbach's conjecture is wrong.");
        }
        
        // sc.close();
	}
}