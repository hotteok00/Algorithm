#include <stdio.h>
#include <math.h>

int main(void) {
	double x1, y1, r1, x2, y2, r2;
	int t;
	scanf("%d", &t);

	double de_x, de_y, de;
	for (int i = 0; i < t; i++) {
		scanf("%lf %lf %lf %lf %lf %lf", &x1, &y1, &r1, &x2, &y2, &r2);
		de_x = pow(x1 - x2, 2);
		de_y = pow(y1 - y2, 2);
		de = sqrt(de_x + de_y);
		
		if (de_x == 0 && de_y == 0) {
			if (r1 == r2) printf("-1\n");
			else printf("0\n");
		}
		else if (r1 > de) {
			if (de + r2 < r1 || r2 > de + r1) printf("0\n");
			else if (r1 == r2 + de || r2 == de + r1) printf("1\n");
			else printf("2\n");
		}
		else if (r1 < de) {
			if (de > r2 + r1 || de + r1 < r2)printf("0\n");
			else if (de == r1 + r2 || de + r1 == r2)printf("1\n");
			else printf("2\n");
		}
		else {
			if (de + r1 == r2) printf("1\n");
			else if (de + r1 < r2) printf("0\n");
			else printf("2\n");
		}
	}

	return 0;
}