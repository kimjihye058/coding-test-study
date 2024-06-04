class Solution {
    public String solution(String my_string, int n) {
        String answer = "";
        for(int i=0; i<my_string.length(); i++)
            answer = my_string.substring(my_string.length()-n);
            // .substring()은 문자열을 특정 부분부터 출력하게 해주는 메소드
        return answer;
    }
}