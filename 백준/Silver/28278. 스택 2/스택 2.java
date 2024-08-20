import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Stack;


public class Main{
    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());

        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            int action = Integer.parseInt(st.nextToken());
            switch (action) {
                case 1:
                    stack.add(Integer.parseInt(st.nextToken()));
                    continue;
                case 2:
                    if (stack.isEmpty()) {
                        sb.append("-1").append("\n");
                        continue;
                    }
                    else {
                        sb.append(stack.pop()).append("\n");
                        continue;
                    }
                case 3:
                    sb.append(stack.size()).append("\n");
                    continue;

                case 4:
                    if (stack.isEmpty()) {
                        sb.append(1).append("\n");
                        continue;
                    }
                    else {
                        sb.append(0).append("\n");
                        continue;
                    }
                case 5:
                    if (stack.isEmpty()) {
                        sb.append("-1").append("\n");
                        continue;
                    }
                    else {
                        sb.append(stack.get(stack.size()-1)).append("\n");
                        continue;
                    }
            }
        }

        System.out.println(sb);

    }
}