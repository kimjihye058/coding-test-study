class Solution {
    public long solution(long n) {
		long answer = 0;

		while(answer * answer < n){
			answer++;
		}

		if(answer * answer == n){
			answer++;
			answer*=answer;
		}else{
			answer = -1;
		}
		return answer;
    }
}