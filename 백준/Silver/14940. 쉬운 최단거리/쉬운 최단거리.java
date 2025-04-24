import java.awt.Point;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Queue;
import java.util.LinkedList;

public class Main {

    static StringBuilder sb = new StringBuilder();
    static int n, m;
    static int[][] map;
    static int[][] visited;
    static int[] dr = {0, 0, 1, -1};
    static int[] dc = {1, -1, 0, 0};
    static Queue<Point> q = new LinkedList<>();

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        map = new int[n][m];
        visited = new int[n][m];

        for (int i = 0; i < n ; i++ ) {
            StringTokenizer str = new StringTokenizer(br.readLine());
            for (int j = 0 ; j < m ; j++ ) {
                map[i][j] = Integer.parseInt(str.nextToken());
            }
        }

        int a = 0;
        int b = 0;

        for (int i = 0; i < n ; i++ ) {
            for (int j = 0 ; j < m ; j++ ) {
                if (map[i][j] == 2) {
                    a = i;
                    b = j;
                }
            }
        }

        bfs(a,b);
        for (int i = 0; i < n ; i++ ) {
            for (int j = 0 ; j < m ; j++ ) {
                if (map[i][j] == 0) {
                    sb.append(0).append(" ");
                }
                else if (map[i][j] == 1 && visited[i][j] == 0) {
                    sb.append(-1).append(" ");
                }
                else {
                    sb.append(visited[i][j]).append(" ");
                }
            }
            sb.append('\n');
        }

        System.out.println(sb);

    }

    public static void bfs(int a, int b) {
        q.add(new Point(a, b));

        while(!q.isEmpty()) {
            Point curr = q.poll();
            for (int r = 0; r < 4; r++) {
                int sr = curr.x + dr[r];
                int sc = curr.y + dc[r];
                if (sr < 0 || n <= sr || sc < 0 || m <= sc) continue;
                if (map[sr][sc] == 1 && visited[sr][sc] == 0) {
                    visited[sr][sc] = visited[curr.x][curr.y] + 1;
                    q.add(new Point(sr, sc));
                }
            }
        }
    }
}
