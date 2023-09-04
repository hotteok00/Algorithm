import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();
    int M = sc.nextInt();
    int[] busket = new int[N];

    for(int i=0; i<M; i++) {
      int start = sc.nextInt();
      int end = sc.nextInt();
      int num = sc.nextInt();
      for(int j = start - 1; j < end; j++) {
        busket[j] = num;
      }
    }
    
    for(int i=0; i<N; i++) System.out.print(busket[i] + " ");

    sc.close();
  }
}