import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;
import java.util.Deque;
import java.util.LinkedList;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        Deque<Integer> queue = new LinkedList<>();

        int n = Integer.parseInt(br.readLine());

        StringTokenizer command;

        while(n-- > 0) {
            command = new StringTokenizer(br.readLine(), " ");
            switch(command.nextToken()) {

                case "push":
                    queue.offer(Integer.parseInt(command.nextToken()));
                    break;

                case "pop":
                    Integer num = queue.poll();
                    if (num == null) {
                        sb.append(-1).append('\n');
                    }
                    else {
                        sb.append(num).append('\n');
                    }
                    break;

                case "size":
                    sb.append(queue.size()).append('\n');
                    break;

                case "empty":
                    if (queue.isEmpty()) {
                        sb.append(1).append('\n');
                    }
                    else {
                        sb.append(0).append('\n');
                    }
                    break;

                case "front":
                    Integer num1 = queue.peek();
                    if (num1==null) {
                        sb.append(-1).append('\n');
                    }
                    else {
                        sb.append(num1).append('\n');
                    }
                    break;

                case "back":
                    Integer num2 = queue.peekLast();
                    if (num2==null) {
                        sb.append(-1).append('\n');
                    }
                    else {
                        sb.append(num2).append('\n');
                    }
                    break;
            }
        }

        System.out.println(sb);

    }
}
