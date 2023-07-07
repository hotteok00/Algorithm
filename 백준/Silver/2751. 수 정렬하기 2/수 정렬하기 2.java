import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.Collections;
import java.util.ArrayList;

public class Main {
	public static void main(String[] args) throws IOException {
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        int length = Integer.parseInt(reader.readLine());
        ArrayList<Integer> arr = new ArrayList<>(length);
        
        for(int i = 0; i < length; i++) arr.add(Integer.parseInt(reader.readLine()));
        
        Collections.sort(arr);
        
        for(int i : arr) sb.append(i).append('\n');
        
        System.out.println(sb);
    }
}