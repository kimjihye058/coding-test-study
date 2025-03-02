import java.util.*;

class Solution {
    public int solution(int[] numbers) {
        int totalSum = 45;
        int numbersSum = 0;
        
        for (int num : numbers) {
            numbersSum += num;
        }
        
        return totalSum - numbersSum;
    }
}