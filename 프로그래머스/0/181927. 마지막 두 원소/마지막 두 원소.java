class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = new int[num_list.length+1];
        int last = num_list[num_list.length - 1];  // 마지막 원소
        int lastb = num_list[num_list.length - 2];  // 마지막 원소에서 그 전 원소
        for(int i=0; i<num_list.length; i++)
            answer[i] = num_list[i];
        if(last > lastb) 
            answer[num_list.length] = last - lastb;
        else
            answer[num_list.length] = last*2;
        return answer;
    }
}