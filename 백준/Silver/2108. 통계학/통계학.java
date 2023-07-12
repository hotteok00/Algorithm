import java.util.*;
import java.io.*;

class Main {
  public static void main(String[] args) throws IOException {
    StringBuilder sb = new StringBuilder();
    BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

    int N = Integer.parseInt(br.readLine());
    HashMap<Integer, Integer> hm = new HashMap<>();

    int sum = 0;
    int median = 0;
    int freq = 0;
    int range = 0;

    for (int i = 0; i < N; i++) {
      int tmp = Integer.parseInt(br.readLine());
      hm.put(tmp, hm.getOrDefault(tmp, 0) + 1);
      sum += tmp;
    }

    Object[] keys = hm.keySet().toArray();
    Arrays.sort(keys);

    int l = keys.length;
    int cnt = 0;
    int max = 0;
    boolean flag = true;
    for (int i = 0; i < l; i++) {
      int key = (int) keys[i];

      if (i == 0)
        range = key;
      if (i == l - 1)
        range = key - range;

      int k = hm.get(key);
      if (k >= max) {
        if (k > max) {
          max = k;
          freq = key;
          flag = true;
        } else if (k == max && flag) {
          max = k;
          freq = key;
          flag = false;
        }
      }

      for (int j = 0; j < k; j++)
        if (++cnt == (N + 1) / 2)
          median = key;
    }

    System.out.println((Math.round((double) sum / N))); // 산술평균
    System.out.println(median); // 중앙값
    System.out.println(freq); // 최빈값
    System.out.println(range); // 범위
  }
}