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

        LinkedList<Integer> deque = new LinkedList<>();

        while (n-- > 0) {
            st = new StringTokenizer(br.readLine());
            String commend = st.nextToken();
            switch (commend) {
                case "push_front":
                    deque.addFirst(Integer.parseInt(st.nextToken()));
                    continue;
                case "push_back":
                    deque.add(Integer.parseInt(st.nextToken()));
                    continue;

                case "pop_front":
                    if (!deque.isEmpty()) {
                        sb.append(deque.pollFirst()).append("\n");
                        continue;
                    }
                    else {
                        sb.append("-1").append("\n");
                        continue;
                    }
                case "pop_back":
                    if (!deque.isEmpty()) {
                        sb.append(deque.pollLast()).append("\n");
                        continue;
                    }
                    else {
                        sb.append("-1").append("\n");
                        continue;
                    }

                case "size":
                    sb.append(deque.size()).append("\n");
                    continue;

                case "empty":
                    if (deque.isEmpty()) {
                        sb.append(1).append("\n");
                        continue;
                    }
                    else {
                        sb.append(0).append("\n");
                        continue;
                    }
                case "front":
                    if (deque.isEmpty()) {
                        sb.append("-1").append("\n");
                        continue;
                    }
                    else {
                        sb.append(deque.peekFirst()).append("\n");
                        continue;
                    }

                case "back":
                    if (deque.isEmpty()) {
                        sb.append("-1").append("\n");
                        continue;
                    }
                    else {
                        sb.append(deque.peekLast()).append("\n");
                        continue;
                    }
            }
        }

        System.out.println(sb);


    }
}