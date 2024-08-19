import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main{


    public static void main(String [] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int [][] arr = new int [n][m];

        for (int i =0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j =0; j < m; j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i =0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j =0; j < m; j++) {
                arr[i][j] = arr[i][j] + Integer.parseInt(st.nextToken());
                if (j!=m-1){
                    sb.append(arr[i][j]).append(" ");
                }
                else {
                    sb.append(arr[i][j]);
                }
            }
            if (i!=n-1){
                sb.append("\n");
            }

        }

        System.out.println(sb);
    }
}