class Solution {
    public int[] solution(String[] strlist) {
        int[] answer = new int [strlist.length];
        int len = strlist.length;
        for(int i=0; i<len; i++){
            answer[i] = strlist[i].length();
        }
        return answer;
    }
}