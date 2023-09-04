import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);

    int N = sc.nextInt();
    int M = sc.nextInt();
    int[] busket = new int[N];
    for(int i=0; i<N; i++) busket[i] = i + 1;

    for(int i=0; i<M; i++) {
      int a = sc.nextInt();
      int b = sc.nextInt();
      swap(a - 1, b - 1, busket);
    }
    
    for(int i=0; i<N; i++) System.out.print(busket[i] + " ");

    sc.close();
  }

  static void swap(int a, int b, int[] arr) {
    int t = arr[a];
    arr[a] = arr[b];
    arr[b] = t;
  }
}