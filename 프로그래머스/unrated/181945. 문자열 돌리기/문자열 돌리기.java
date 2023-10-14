import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String a = sc.next();
        
		for(int i=0; i<a.length(); i++) {
			System.out.println(a.charAt(i));
		}
        // .charAt(i) 함수는 String 타입의 형태에서 사용된다.
        // i 자리에는 int 형 변수를 넣어서 원하는 위치의 문자를 가져올 수 있다.
		
		sc.close();
		
        
        
    }
}