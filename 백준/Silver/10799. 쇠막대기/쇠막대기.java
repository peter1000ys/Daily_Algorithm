import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;

// ")"를 만나고 스택 맨 위 값이 "("일 경우 스택의 사이즈 만큼 더 해준다.
// ")"를 만나고 스택 맨 위 값이 ")" 인 경우 하나의 막대기가 끝난 것으로 +1민 해준다.

public class Main{
    public static void main(String [] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String input = br.readLine();

        int result = 0;
        int last = 0;
        LinkedList<Character> stack = new LinkedList<>();

        for (int i = 0; i < input.length(); i++) {
            if (input.charAt(i) == '(') {
                stack.add('(');
                last = i;
            }
            else if (input.charAt(i) == ')') {

                if (!stack.isEmpty()) {
                    if (stack.peekLast() == '(' && last == i-1) {
                        stack.removeLast();
                        result += stack.size();

                    }
                    else {
                        result += 1;
                        stack.removeLast();


                    }

                }
            }
        }

        System.out.println(result);



    }
}