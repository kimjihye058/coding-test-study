class Solution {
    public String solution(String[] seoul) {
        String answer = "";
        for(int i=0; i<seoul.length; i++){
            if(seoul[i].equals("Kim")){
                answer = String.format("김서방은 %d에 있다", i);
            }
        }
        return answer;
    }
}