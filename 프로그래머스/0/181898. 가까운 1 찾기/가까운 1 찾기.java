class Solution {
    public int solution(int[] arr, int idx) {
        for(int i=0; i<arr.length; i++){
            if(arr[i] == 1 && i>=idx){
                return i;
            }
        }
        return -1;
    }
}