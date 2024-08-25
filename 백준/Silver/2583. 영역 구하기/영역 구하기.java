import java.io.*;
import java.util.*;


public class Main {
    // main과 dfs 모두 사용할 것들
    public static int [][] board;
    public static int n;
    public static int m;
    public static int size;
    public static int[] dx = {0, 0, 1, -1};
    public static int[] dy = {1, -1, 0, 0};

    public static void main(String[] args) throws IOException {
        StringBuilder sb = new StringBuilder();
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        // 입력 받은 n,m에 맞는 배열
        board = new int[n][m];
        ArrayList<Integer> result = new ArrayList<>();


        // k개의 구역 입력 받음
        for (int i = 0; i < k; i++) {
            st = new StringTokenizer(br.readLine());
            int x1 = Integer.parseInt(st.nextToken());
            int y1 = Integer.parseInt(st.nextToken());
            int x2 = Integer.parseInt(st.nextToken());
            int y2 = Integer.parseInt(st.nextToken());

            for (int y = y1; y < y2; y++) {
                for (int x = x1; x < x2; x++) {
                    board[y][x] = 1;
                }
            }
        }
        for (int a = 0; a < n; a++) {
            for (int b = 0; b < m; b++) {
                if (board[a][b] == 0) {
                    size = 1;
                    dfs(a, b);
                    result.add(size);
                }
            }
        }
        Collections.sort(result);

        sb.append(result.size()).append("\n");
        for (int r : result) {
            sb.append(r).append(" ");
        }

        System.out.println(sb);

    }

    public static void dfs(int y, int x) {
        board[y][x] = 1;

        for (int i = 0; i < 4; i++) {
            int nx = x + dx[i];
            int ny = y + dy[i];

            if ( 0<= nx && nx < m && 0<= ny && ny < n && board[ny][nx] == 0 ) {
                size++;
                dfs(ny, nx);
            }
        }
    }
}