import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.LinkedList;



public class Main{
    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        StringBuilder sb = new StringBuilder();

        int n = Integer.parseInt(st.nextToken());

        LinkedList<Integer> queue = new LinkedList<>();

        while (n-- > 0) {
            st = new StringTokenizer(br.readLine());
            String commend = st.nextToken();
            switch (commend) {
                case "push":
                    queue.add(Integer.parseInt(st.nextToken()));
                    continue;

                case "pop":
                    if (!queue.isEmpty()) {
                        sb.append(queue.pollFirst()).append("\n");
                        continue;
                    }
                    else {
                        sb.append("-1").append("\n");
                        continue;
                    }


                case "size":
                    sb.append(queue.size()).append("\n");
                    continue;

                case "empty":
                    if (queue.isEmpty()) {
                        sb.append(1).append("\n");
                        continue;
                    }
                    else {
                        sb.append(0).append("\n");
                        continue;
                    }
                case "front":
                    if (queue.isEmpty()) {
                        sb.append("-1").append("\n");
                        continue;
                    }
                    else {
                        sb.append(queue.peekFirst()).append("\n");
                        continue;
                    }

                case "back":
                    if (queue.isEmpty()) {
                        sb.append("-1").append("\n");
                        continue;
                    }
                    else {
                        sb.append(queue.peekLast()).append("\n");
                        continue;
                    }
            }
        }

        System.out.println(sb);


    }
}