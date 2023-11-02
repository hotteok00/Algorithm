import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
      
    int k = sc.nextInt();
    int n = sc.nextInt();
      
    int[] arr = new int[k];
    long max=0;
    long min=0;
    long mid=0;
    
    for(int i=0; i<k; i++) {
      arr[i] = sc.nextInt();
      if(max < arr[i]) max = arr[i];
    }

    max++;
    
    while(max > min) {
      mid = (max+min)/2;
      long tmp=0;
      
      for(Integer i : arr) tmp += (i/mid);
      
      if (tmp < n) max = mid;
      else min = mid + 1;
    }
    System.out.println(min-1);
      
    sc.close();
  }
} 