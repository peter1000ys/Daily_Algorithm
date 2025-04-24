import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

import java.util.StringTokenizer;
import java.util.Deque;
import java.util.LinkedList;
import java.util.ArrayList;


public class Main {
    static StringBuilder sb = new StringBuilder();
    static int n;
    static ArrayList<Integer>[] adjl;
    static int[] visited;

    static Deque<Integer> q = new LinkedList<>();

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        visited = new int[n+1];
        adjl = new ArrayList[n+1];
        for (int i = 1 ; i <= n ; i++ ) {
            adjl[i] = new ArrayList<>();
        }

        for(int i = 0 ; i < n-1; i++) {
            StringTokenizer str = new StringTokenizer(br.readLine());
            int a = Integer.parseInt(str.nextToken());
            int b = Integer.parseInt(str.nextToken());
            adjl[a].add(b);
            adjl[b].add(a);
        }

        bfs(1);

        for (int i = 2 ; i < n+1; i++ ) {
            sb.append(visited[i]);
            sb.append('\n');
        }

        System.out.println(sb);


    }

    public static void bfs(int start) {
        q.add(start);

        while (!q.isEmpty()) {
            start = q.poll();

            for (int curr : adjl[start]) {
                if (visited[curr] == 0) {
                    visited[curr] = start;
                    q.add(curr);
                }
            }
        }
    }
}
