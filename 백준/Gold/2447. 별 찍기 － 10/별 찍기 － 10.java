import java.util.Scanner;

class Main {
  public static void main(final String[] args) {
    final Scanner sc = new Scanner(System.in);
    final int n = sc.nextInt();

    final char[][] m = new char[n][n];
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
        m[i][j] = '*';

    for(int i = n; i >= 3; ) {
      int a = i / 3;
      for(int j = a; j<n; j += 3*a) {
        for(int k = a; k<n; k += 3*a) {
          // System.out.println("j, k : "+j+","+k);
          int tmp_j = j;
          int tmp_k = k;
          
          int l_j = j+a;
          int l_k = k+a;
          for(j = tmp_j; j<l_j; j++) {
            for(k = tmp_k; k<l_k; k++) {
              // System.out.println("j, k : "+j+","+k);
              m[j][k] = ' ';
            }
          }

          j = tmp_j;
          k = tmp_k;
        }
      }
      i = a;
    }

    printStar(n, m);

    sc.close();
  }

  static void printStar(int n, char[][] m) {
    StringBuilder sb = new StringBuilder();
    for (int i = 0; i < n; i++) {
      for (int j = 0; j < n; j++)
        sb.append(m[i][j]);
      sb.append('\n');
    }
    System.out.println(sb.toString());
  }
}