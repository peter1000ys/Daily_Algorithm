import java.util.ArrayList;
import java.util.StringTokenizer; 

class Solution {
    public ArrayList<String> solution(String my_string) {
        StringTokenizer st = new StringTokenizer(my_string);
        ArrayList<String> answer = new ArrayList<>();
        while (st.hasMoreTokens()) {
            answer.add(st.nextToken());
        }
        return answer;
    }
}