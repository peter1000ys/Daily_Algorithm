import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;


public class Main{


    public static void main(String [] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st;
        StringBuilder sb = new StringBuilder();


        int [][] arr = new int [9][9];

        int max_num = 0;
        int max_x = 0;
        int max_y = 0;

        for (int i =0; i < 9; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j =0; j < 9; j++) {
                int temp = Integer.parseInt(st.nextToken());
                if (max_num < temp) {
                    max_x = j;
                    max_y = i;
                    max_num = temp;
                }
            }
        }
        sb.append(max_num).append("\n").append(max_y+1).append(" ").append(max_x+1);
        System.out.println(sb);
    }


}