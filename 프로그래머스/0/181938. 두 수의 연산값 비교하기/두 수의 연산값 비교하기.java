class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        //정수인 숫자를 문자로 변환
        String aa = String.valueOf(a);
        String bb = String.valueOf(b);

        //문자열인 두 숫자를 합쳐서 정수로 변환
        int aabb = Integer.valueOf(aa + bb);
        int aabb2 = 2 * a * b;

        if (aabb < aabb2)
            answer = aabb2;
        else
            answer = aabb;
        
        return answer;
    }
}