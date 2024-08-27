import java.io.*;
import java.util.*;


public class Main {
    // main과 dfs 모두 사용할 것들
    public static List<List<Integer>> adjl =  new ArrayList<>();
    // 정점의 개수 n
    public static int n;
    // 간선의 개수 m
    public static int m;
    // 시작 정점 v
    public static int v;

    public static boolean [] visited_d;
    public static boolean [] visited_b;

    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        v= Integer.parseInt(st.nextToken());

        visited_d = new boolean[n+1];
        visited_b = new boolean[n+1];

        // 인접 리스트 생성
        for (int i = 0; i < n+1; i++) {
            adjl.add(new ArrayList<>());
        }

        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            adjl.get(a).add(b);
            adjl.get(b).add(a);
        }

        for (int i =0; i < n+1; i++) {
            Collections.sort(adjl.get(i));
        }

        dfs(v);
        sb.append("\n");
        bfs(v);
        System.out.println(sb);


    }

    public static void dfs(int root) {
        visited_d[root] = true;
        sb.append(root).append(" ");
        for (int i : adjl.get(root)) {
            if (!visited_d[i]) {
                dfs(i);
            }
        }
    }

    public static void bfs(int root) {
        Queue<Integer> q = new LinkedList<>();
        q.add(root);
        visited_b[root] = true;
        while (!q.isEmpty()) {
            int v = q.poll();
            sb.append(v).append(" ");
            for (int i : adjl.get(v)) {
                if (!visited_b[i]) {
                    visited_b[i] = true;
                    q.add(i);
                }
            }
        }
    }
}