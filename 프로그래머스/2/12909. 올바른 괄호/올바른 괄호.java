class Solution {

    boolean solution(String s) {
        int openCount = 0;
        int closeCount = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == '(') {
                openCount++;
            } else if (s.charAt(i) == ')') {
                closeCount++;
            }
            if (openCount < closeCount) {
                return false;
            }
        }
        if (openCount == closeCount) {
            return true;
        }
        return false;
    }
}