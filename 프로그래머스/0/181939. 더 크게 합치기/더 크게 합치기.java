class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        
        String ab = String.valueOf(a) + String.valueOf(b);
        String ba = String.valueOf(b) + String.valueOf(a);
        // String -> int  변환 : Integer.parseInt()
        // int -> String  변환 : String.valueOf()
        
        if (Integer.parseInt(ab) >= Integer.parseInt(ba)) {
            return Integer.parseInt(ab);
        } else {
            return Integer.parseInt(ba);
        }
    }
}