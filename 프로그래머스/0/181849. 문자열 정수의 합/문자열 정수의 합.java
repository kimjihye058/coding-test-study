class Solution {
    public int solution(String str) {
        int answer = 0;
        for(int i = 0; i < str.length(); i++){
            answer += Integer.parseInt(str.substring(i, i+1));
        }
        return answer;
    }
}
