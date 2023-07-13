import java.util.*;

public class Main {
	
	public static String grade_iToS(int grade) {
		String grade_S;
		if(grade > 96) grade_S = "A+";
		else if(grade > 89) grade_S = "A";
		else if(grade > 86) grade_S = "B+";
		else if(grade > 79) grade_S = "B";
		else if(grade > 76) grade_S = "C+";
		else if(grade > 69) grade_S = "C";
		else if(grade > 66) grade_S = "D+";
		else if(grade > 59) grade_S = "D";
		else grade_S = "F";
		
		return grade_S;
	}

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int n = sc.nextInt();
		sc.nextLine();
		String name;
		int grade;
		String grade_S;
		for(int i = 0; i < n; i++) {
			name = sc.next();
			grade = sc.nextInt();
			grade_S = grade_iToS(grade);
			System.out.println(name + " " + grade_S);
		}
	}

}
