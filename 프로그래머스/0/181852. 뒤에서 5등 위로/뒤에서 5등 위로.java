import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length - 5];
        Arrays.sort(num_list);  // 오름차순
        
        for (int i = 5; i < num_list.length; i++) {
            answer[i - 5] = num_list[i];        // 오름차순에서 마지막 5개를 제외한 수
        }
        
        return answer;
    }
}