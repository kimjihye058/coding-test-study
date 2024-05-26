import java.util.Arrays;

class Solution {
    public int solution(int[] numbers) {
        int answer = 0;
        Arrays.sort(numbers);
        int n = numbers.length;
        int max1 = numbers[n - 1];
        int max2 = numbers[n - 2];
        answer = max1*max2;
        return answer;
    }
}