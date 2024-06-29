import java.util.*;

class Solution {
    public String[] solution(String[] todo_list, boolean[] finished) {
        ArrayList<String> answerList = new ArrayList<>();
        for(int i=0; i<todo_list.length; i++){
            if(finished[i] == false)
                answerList.add(todo_list[i]);
        }
        String[] answer = new String[answerList.size()];
        answer = answerList.toArray(answer);
        
        return answer;
    }
}