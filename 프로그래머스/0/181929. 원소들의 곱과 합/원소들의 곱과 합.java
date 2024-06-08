class Solution {
    public int solution(int[] num_list) {
        int sum=0;
        int mul=1;
        for(int i=0; i<num_list.length; i++){
            sum += num_list[i];
            mul *= num_list[i];
        }
        if(sum*sum>mul)
            return 1;
        else
            return 0;
    }
}